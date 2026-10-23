"""
Inference Pipeline for Plant Leaf Disease Detection
Integrates deep transfer learning (MobileNetV2 PlantVillage),
automated crop filtering, confidence thresholding, and OpenCV foliar lesion segmentation.
"""

import os
from pathlib import Path
from typing import Optional, Dict, Any, List
import numpy as np
import cv2
from PIL import Image
import torch
from torchvision import transforms
from transformers import AutoImageProcessor, AutoModelForImageClassification

from detection.disease_info import DISEASE_CLASSES, get_disease_info, normalize_class_name


ROOT_DIR = Path(__file__).resolve().parent.parent
DEFAULT_MODEL_DIR = ROOT_DIR / "models" / "mobilenetv2_plantvillage"
HF_FALLBACK_MODEL = "LourivalGontijo/plantvillage-mobilenetv2"


def get_device() -> torch.device:
    """Detect Apple Silicon MPS, CUDA, or CPU."""
    if torch.backends.mps.is_available():
        return torch.device("mps")
    elif torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def load_classifier(model_path: Optional[str] = None, device: Optional[torch.device] = None):
    """
    Loads pre-trained PlantVillage deep learning classifier and image preprocessor.
    Prioritizes local trained weights in models/mobilenetv2_plantvillage.
    """
    if device is None:
        device = get_device()

    # Determine local model directory
    if model_path and os.path.isdir(model_path):
        target_path = model_path
    elif DEFAULT_MODEL_DIR.exists() and (DEFAULT_MODEL_DIR / "config.json").exists():
        target_path = str(DEFAULT_MODEL_DIR)
    else:
        target_path = HF_FALLBACK_MODEL

    try:
        processor = AutoImageProcessor.from_pretrained(target_path)
        model = AutoModelForImageClassification.from_pretrained(target_path)
    except Exception as e:
        print(f"Warning loading from {target_path}: {e}. Falling back to HuggingFace hub...")
        processor = AutoImageProcessor.from_pretrained(HF_FALLBACK_MODEL)
        model = AutoModelForImageClassification.from_pretrained(HF_FALLBACK_MODEL)

    model.to(device)
    model.eval()
    return {"model": model, "processor": processor, "device": device}


def generate_lesion_analysis(image_pil: Image.Image):
    """
    Extracts leaf region of interest and highlights necrotic lesions/spots
    using adaptive color-space segmentation (HSV + Lab color difference).
    Returns:
      - annotated_img: image with detected lesion contours
      - heatmap_img: saliency heatmap
      - lesion_percentage: estimated leaf area showing symptoms
    """
    rgb_arr = np.array(image_pil.convert("RGB"))
    bgr_arr = cv2.cvtColor(rgb_arr, cv2.COLOR_RGB2BGR)
    hsv_arr = cv2.cvtColor(bgr_arr, cv2.COLOR_BGR2HSV)

    # Segment overall leaf tissue (green, yellow, brown hues)
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
            cv2.drawContours(annotated, [cnt], -1, (230, 40, 40), 2)

    # Create attention heat map overlay
    heatmap = cv2.applyColorMap(clean_lesion, cv2.COLORMAP_JET)
    heatmap_rgb = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)
    blended = cv2.addWeighted(rgb_arr, 0.65, heatmap_rgb, 0.35, 0)

    return annotated, blended, round(lesion_percentage, 2)


def predict_leaf_disease(
    image_pil: Image.Image,
    model_bundle: Any,
    device: Optional[torch.device] = None,
    crop_filter: Optional[str] = None,
    confidence_threshold: float = 50.0,
    top_k: int = 5
) -> Dict[str, Any]:
    """
    Executes deep learning inference with optional crop family filtering
    and confidence threshold verification.
    """
    # Handle both wrapped bundle and direct PyTorch model
    if isinstance(model_bundle, dict):
        model = model_bundle["model"]
        processor = model_bundle.get("processor")
        device = model_bundle.get("device", device or get_device())
    else:
        model = model_bundle
        processor = None
        if device is None:
            device = get_device()

    rgb_img = image_pil.convert("RGB")

    # Preprocessing
    if processor is not None:
        inputs = processor(rgb_img, return_tensors="pt")
        inputs = {k: v.to(device) for k, v in inputs.items()}
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
    else:
        trans = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        ])
        tensor = trans(rgb_img).unsqueeze(0).to(device)
        with torch.no_grad():
            logits = model(tensor)
            if hasattr(logits, "logits"):
                logits = logits.logits

    probabilities = torch.softmax(logits, dim=-1)[0].cpu().numpy()

    # Extract label mappings
    id2label = getattr(model.config, "id2label", None)
    if id2label is None:
        id2label = {i: cls for i, cls in enumerate(DISEASE_CLASSES)}

    # Build candidates
    all_candidates: List[Dict[str, Any]] = []
    for idx, prob in enumerate(probabilities):
        raw_name = id2label[idx]
        norm_name = normalize_class_name(raw_name)
        info = get_disease_info(norm_name)
        all_candidates.append({
            "idx": idx,
            "class_raw": norm_name,
            "crop": info["crop"],
            "disease_name": info["disease_name"],
            "confidence": float(prob * 100.0),
            "severity": info["severity"],
            "pathogen": info["pathogen"],
            "is_healthy": "healthy" in norm_name.lower()
        })

    # Sort candidates by probability descending
    all_candidates.sort(key=lambda x: x["confidence"], reverse=True)

    # Apply Crop Filter if specified and not 'All Crops'
    filtered_candidates = all_candidates
    if crop_filter and crop_filter != "All Crops":
        crop_clean = crop_filter.lower().strip()
        matched = [
            c for c in all_candidates
            if crop_clean in c["crop"].lower() or crop_clean in c["class_raw"].lower()
        ]
        if matched:
            # Re-normalize probabilities among matched crop classes
            total_filtered_prob = sum(c["confidence"] for c in matched)
            if total_filtered_prob > 0.001:
                filtered_candidates = []
                for c in matched:
                    c_copy = dict(c)
                    c_copy["confidence"] = round((c["confidence"] / total_filtered_prob) * 100.0, 2)
                    filtered_candidates.append(c_copy)
                filtered_candidates.sort(key=lambda x: x["confidence"], reverse=True)
            else:
                filtered_candidates = matched

    # Primary selection
    top_candidate = filtered_candidates[0]
    top_class = top_candidate["class_raw"]
    top_confidence = round(top_candidate["confidence"], 2)
    disease_record = get_disease_info(top_class)
    is_healthy = top_candidate["is_healthy"]

    # Threshold assessment
    is_confident = top_confidence >= confidence_threshold

    # Lesion visual diagnostics
    annotated_img, heatmap_img, lesion_pct = generate_lesion_analysis(rgb_img)

    return {
        "top_class": top_class,
        "top_confidence": top_confidence,
        "is_confident": is_confident,
        "confidence_threshold": confidence_threshold,
        "crop_filter": crop_filter,
        "disease_record": disease_record,
        "candidates": filtered_candidates[:top_k],
        "all_candidates": all_candidates[:top_k],
        "annotated_image": annotated_img,
        "heatmap_image": heatmap_img,
        "lesion_percentage": lesion_pct,
        "is_healthy": is_healthy
    }
