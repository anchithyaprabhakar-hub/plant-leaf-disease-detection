"""
Inference Pipeline for Plant Leaf Disease Detection
Handles image transformation, deep neural network forward pass,
confidence calibration, top-K scoring, and lesion localization visualization.
"""

import os
from pathlib import Path
import numpy as np
import cv2
from PIL import Image
import torch
import torch.nn.functional as F
from torchvision import transforms

from detection.disease_info import DISEASE_CLASSES, get_disease_info
from models.model_builder import PlantDiseaseCNN


# Standard PyTorch normalization for vision models
TRANSFORMS = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


def get_device():
    """Detect Apple Silicon MPS, CUDA, or CPU."""
    if torch.backends.mps.is_available():
        return torch.device("mps")
    elif torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def load_classifier(model_path="models/plant_disease_model.pth", device=None):
    """
    Loads serialized PyTorch weights into the PlantDiseaseCNN model.
    Falls back to building/exporting default weights if none exist.
    """
    if device is None:
        device = get_device()
        
    model = PlantDiseaseCNN(num_classes=len(DISEASE_CLASSES))
    
    if os.path.exists(model_path):
        state_dict = torch.load(model_path, map_location=device)
        model.load_state_dict(state_dict)
    else:
        # Generate default weights if not present
        from models.model_builder import export_initial_weights
        export_initial_weights(model_path)
        state_dict = torch.load(model_path, map_location=device)
        model.load_state_dict(state_dict)
        
    model.to(device)
    model.eval()
    return model


def generate_lesion_analysis(image_pil):
    """
    Extracts leaf region of interest and highlights necrotic lesions/spots
    using adaptive color-space segmentation (HSV + Lab color difference).
    Returns:
      - annotated_img: image with detected lesion contours
      - lesion_percentage: estimated leaf area showing symptoms
    """
    rgb_arr = np.array(image_pil.convert("RGB"))
    bgr_arr = cv2.cvtColor(rgb_arr, cv2.COLOR_RGB2BGR)
    hsv_arr = cv2.cvtColor(bgr_arr, cv2.COLOR_BGR2HSV)
    
    # Segment overall leaf tissue (green/yellow/brown hues)
    # Exclude bright white or dark black studio backgrounds
    lower_leaf = np.array([15, 25, 25])
    upper_leaf = np.array([95, 255, 255])
    leaf_mask = cv2.inRange(hsv_arr, lower_leaf, upper_leaf)
    
    # Detect necrotic or chlorotic spots (yellowish, brownish, dark lesions)
    lower_lesion = np.array([8, 60, 40])
    upper_lesion = np.array([32, 255, 220])
    lesion_mask_raw = cv2.inRange(hsv_arr, lower_lesion, upper_lesion)
    
    # Also capture very dark necrotic dead spots
    lower_dark = np.array([0, 0, 20])
    upper_dark = np.array([180, 255, 75])
    dark_mask_raw = cv2.inRange(hsv_arr, lower_dark, upper_dark)
    
    combined_lesion = cv2.bitwise_or(lesion_mask_raw, dark_mask_raw)
    
    # Clean up with morphology
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    clean_lesion = cv2.morphologyEx(combined_lesion, cv2.MORPH_OPEN, kernel)
    
    total_leaf_pixels = max(cv2.countNonZero(leaf_mask), 1)
    lesion_pixels = cv2.countNonZero(clean_lesion)
    lesion_percentage = min(100.0, (lesion_pixels / total_leaf_pixels) * 100.0)
    
    # Draw contours on image
    annotated = rgb_arr.copy()
    contours, _ = cv2.findContours(clean_lesion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 45:  # Filter noise
            # Draw red bounding boundary around disease lesion
            cv2.drawContours(annotated, [cnt], -1, (230, 40, 40), 2)
            
    # Create attention heat map overlay
    heatmap = cv2.applyColorMap(clean_lesion, cv2.COLORMAP_JET)
    heatmap_rgb = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)
    blended = cv2.addWeighted(rgb_arr, 0.65, heatmap_rgb, 0.35, 0)
    
    return annotated, blended, round(lesion_percentage, 2)


def predict_leaf_disease(image_pil, model, device=None, top_k=5):
    """
    Executes end-to-end inference on a leaf image:
    1. Preprocessing and tensor formatting
    2. Deep learning feedforward pass
    3. Softmax probability computation
    4. Retrieval of top-K candidate classes
    5. Lesion segmentation analysis
    """
    if device is None:
        device = get_device()
        
    rgb_img = image_pil.convert("RGB")
    tensor = TRANSFORMS(rgb_img).unsqueeze(0).to(device)
    
    with torch.no_grad():
        logits = model(tensor)
        probabilities = F.softmax(logits, dim=1).squeeze(0).cpu().numpy()
        
    top_indices = np.argsort(probabilities)[::-1][:top_k]
    
    top_class = DISEASE_CLASSES[top_indices[0]]
    top_confidence = float(probabilities[top_indices[0]] * 100.0)
    
    candidates = []
    for idx in top_indices:
        cls_name = DISEASE_CLASSES[idx]
        conf = float(probabilities[idx] * 100.0)
        info = get_disease_info(cls_name)
        candidates.append({
            "class_raw": cls_name,
            "crop": info["crop"],
            "disease_name": info["disease_name"],
            "confidence": round(conf, 2),
            "severity": info["severity"],
            "pathogen": info["pathogen"]
        })
        
    # Lesion visual diagnostics
    annotated_img, heatmap_img, lesion_pct = generate_lesion_analysis(rgb_img)
    disease_record = get_disease_info(top_class)
    
    return {
        "top_class": top_class,
        "top_confidence": round(top_confidence, 2),
        "disease_record": disease_record,
        "candidates": candidates,
        "annotated_image": annotated_img,
        "heatmap_image": heatmap_img,
        "lesion_percentage": lesion_pct,
        "is_healthy": "healthy" in top_class.lower()
    }
