"""
Pipeline Verification Test
Verifies model loading, tensor transformations, sample image inference,
and lesion segmentation.
"""

from pathlib import Path
from PIL import Image
from detection.disease_classifier import load_classifier, predict_leaf_disease, get_device
from detection.disease_info import DISEASE_CLASSES

def test_pipeline():
    print("1. Testing device detection...")
    device = get_device()
    print(f"   Detected compute device: {device}")
    
    print("2. Testing model loading...")
    model = load_classifier("models/plant_disease_model.pth", device=device)
    assert model is not None, "Model failed to load!"
    print(f"   Model loaded successfully with {len(DISEASE_CLASSES)} classes.")
    
    print("3. Testing sample leaf inference...")
    sample_path = Path("assets/sample_leaves/tomato_early_blight.jpg")
    assert sample_path.exists(), f"Sample image not found at {sample_path}!"
    
    img = Image.open(sample_path)
    result = predict_leaf_disease(img, model, device=device)
    
    print(f"   Top Predicted Class: {result['top_class']}")
    print(f"   Confidence: {result['top_confidence']}%")
    print(f"   Lesion Foliar Coverage: {result['lesion_percentage']}%")
    print(f"   Disease Record: {result['disease_record']['disease_name']}")
    print(f"   Symptoms Count: {len(result['disease_record']['symptoms'])}")
    print(f"   Organic Remedies Count: {len(result['disease_record']['organic_remedies'])}")
    print(f"   Chemical Remedies Count: {len(result['disease_record']['chemical_control'])}")
    print("Pipeline verification PASSED successfully!")

if __name__ == "__main__":
    test_pipeline()
