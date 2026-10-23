"""
Plant Leaf Disease Deep Learning Model Architecture
Defines the deep convolutional neural network (MobileNetV2 Transfer Learning and Custom PlantCNN)
for multi-class agricultural plant foliar disease diagnosis.
"""

import os
from pathlib import Path
import torch
import torch.nn as nn
import torchvision.models as models

try:
    from detection.disease_info import DISEASE_CLASSES
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    from detection.disease_info import DISEASE_CLASSES


class PlantDiseaseCNN(nn.Module):
    """
    Custom 5-Block Deep Convolutional Neural Network for Plant Leaf Disease Classification.
    Features:
      - Multi-scale convolutional feature extraction
      - Batch Normalization for gradient stabilization
      - Dropout for regularization and preventing overfitting
      - Adaptive Average Pooling for arbitrary resolution tolerance
    """
    def __init__(self, num_classes=len(DISEASE_CLASSES)):
        super().__init__()
        
        self.features = nn.Sequential(
            # Block 1: Low-level texture & edge extraction
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.Conv2d(32, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),  # 112 x 112
            nn.Dropout2d(0.1),

            # Block 2: Intermediate foliar lesion patterns
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),  # 56 x 56
            nn.Dropout2d(0.15),

            # Block 3: Higher-order necrotic spot & chlorosis features
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.Conv2d(128, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),  # 28 x 28
            nn.Dropout2d(0.2),

            # Block 4: Complex multi-leaf context & disease boundaries
            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),  # 14 x 14
            nn.Dropout2d(0.25),

            # Block 5: Deep semantic foliar disease abstractions
            nn.Conv2d(256, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),  # 7 x 7
            nn.Dropout2d(0.3),
        )
        
        self.global_pool = nn.AdaptiveAvgPool2d((1, 1))
        
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(inplace=True),
            nn.Dropout(0.4),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.global_pool(x)
        x = self.classifier(x)
        return x


def build_mobilenet_v2(num_classes=len(DISEASE_CLASSES), pretrained=False):
    """
    Builds a MobileNetV2 architecture with inverted residual bottlenecks
    tailored for edge-ready plant disease classification.
    """
    model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT if pretrained else None)
    in_features = model.classifier[1].in_features
    model.classifier = nn.Sequential(
        nn.Dropout(0.3),
        nn.Linear(in_features, 512),
        nn.ReLU(inplace=True),
        nn.Dropout(0.2),
        nn.Linear(512, num_classes)
    )
    return model


def get_default_model(model_path=None, device="cpu"):
    """
    Loads or initializes the trained Plant Disease Deep Learning model.
    Prioritizes models/mobilenetv2_plantvillage.
    """
    from transformers import AutoModelForImageClassification
    target = model_path if model_path and os.path.exists(model_path) else "models/mobilenetv2_plantvillage"
    try:
        model = AutoModelForImageClassification.from_pretrained(target)
    except Exception:
        model = AutoModelForImageClassification.from_pretrained("LourivalGontijo/plantvillage-mobilenetv2")
    
    model.to(device)
    model.eval()
    return model


def export_initial_weights(output_path="models/plant_disease_model.pth"):
    """
    Ensures pre-trained high-accuracy weights are serialized to disk.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    from transformers import AutoModelForImageClassification
    try:
        model = AutoModelForImageClassification.from_pretrained("models/mobilenetv2_plantvillage")
    except Exception:
        model = AutoModelForImageClassification.from_pretrained("LourivalGontijo/plantvillage-mobilenetv2")
    torch.save(model.state_dict(), output_path)
    print(f"Exported model checkpoint successfully to {output_path}")
    return output_path


if __name__ == "__main__":
    export_initial_weights()
