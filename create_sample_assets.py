"""
Generates synthetic leaf images with botanical textures, veins, and lesion characteristics
for local demonstration, testing, and offline evaluation.
"""

import os
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter


def create_leaf_canvas(width=320, height=320, leaf_color=(45, 140, 55)):
    """Draws a base leaf with stem and vascular veins."""
    img = Image.new("RGB", (width, height), (245, 245, 240))
    draw = ImageDraw.Draw(img)
    
    cx, cy = width // 2, height // 2
    
    # Leaf outline ellipse / oval
    leaf_bbox = [cx - 100, cy - 130, cx + 100, cy + 120]
    draw.ellipse(leaf_bbox, fill=leaf_color, outline=(25, 95, 35), width=2)
    
    # Stem
    draw.line([cx, cy + 120, cx, cy + 155], fill=(70, 110, 45), width=5)
    
    # Main midrib vein
    draw.line([cx, cy - 125, cx, cy + 120], fill=(80, 175, 75), width=3)
    
    # Lateral secondary veins
    for dy in range(-90, 90, 25):
        y = cy + dy
        draw.line([cx, y, cx - 75, y - 18], fill=(70, 160, 65), width=2)
        draw.line([cx, y, cx + 75, y - 18], fill=(70, 160, 65), width=2)
        
    return img


def add_early_blight_lesions(img):
    """Adds concentric target-board dark brown lesions with yellow halos."""
    draw = ImageDraw.Draw(img)
    spots = [(140, 130, 22), (190, 180, 18), (120, 210, 15)]
    for sx, sy, r in spots:
        # Yellow chlorotic halo
        draw.ellipse([sx - r - 8, sy - r - 8, sx + r + 8, sy + r + 8], fill=(195, 190, 40))
        # Concentric rings
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(90, 50, 25))
        draw.ellipse([sx - r + 4, sy - r + 4, sx + r - 4, sy + r - 4], fill=(60, 35, 15))
        draw.ellipse([sx - r + 8, sy - r + 8, sx + r - 8, sy + r - 8], fill=(110, 65, 30))
    return img.filter(ImageFilter.GaussianBlur(radius=0.7))


def add_late_blight_lesions(img):
    """Adds irregular dark brown water-soaked necrotic patches with pale fungal margins."""
    draw = ImageDraw.Draw(img)
    # Large water-soaked patch
    draw.polygon([(110, 80), (180, 70), (220, 130), (160, 170), (100, 130)], fill=(45, 55, 35))
    draw.polygon([(120, 90), (170, 80), (210, 125), (150, 155), (110, 120)], fill=(30, 25, 20))
    # Margin mold specks
    for px, py in [(98, 135), (225, 135), (165, 175), (115, 75)]:
        draw.ellipse([px-4, py-4, px+4, py+4], fill=(215, 225, 215))
    return img.filter(ImageFilter.GaussianBlur(radius=1.0))


def add_rust_pustules(img):
    """Adds cinnamon-brown powdery rust pustules."""
    draw = ImageDraw.Draw(img)
    np.random.seed(42)
    for _ in range(35):
        rx = int(np.random.uniform(90, 230))
        ry = int(np.random.uniform(70, 250))
        rad = int(np.random.uniform(3, 7))
        draw.ellipse([rx - rad, ry - rad, rx + rad, ry + rad], fill=(185, 75, 20), outline=(130, 45, 10))
    return img.filter(ImageFilter.GaussianBlur(radius=0.5))


def add_apple_scab_lesions(img):
    """Adds olive-green to dark velvety circular scab spots."""
    draw = ImageDraw.Draw(img)
    spots = [(130, 110, 14), (180, 140, 18), (145, 200, 20), (210, 190, 12)]
    for sx, sy, r in spots:
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(45, 55, 25), outline=(25, 35, 15), width=2)
        # Inner velvety texture
        draw.ellipse([sx - r + 3, sy - r + 3, sx + r - 3, sy + r - 3], fill=(60, 70, 35))
    return img.filter(ImageFilter.GaussianBlur(radius=0.6))


def generate_all_samples():
    base_dir = Path(__file__).resolve().parent
    assets_dir = base_dir / "assets" / "sample_leaves"
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    samples = {
        "tomato_early_blight.jpg": add_early_blight_lesions(create_leaf_canvas(leaf_color=(50, 135, 45))),
        "tomato_late_blight.jpg": add_late_blight_lesions(create_leaf_canvas(leaf_color=(45, 130, 40))),
        "tomato_healthy.jpg": create_leaf_canvas(leaf_color=(35, 155, 50)),
        "potato_early_blight.jpg": add_early_blight_lesions(create_leaf_canvas(leaf_color=(55, 145, 45))),
        "potato_late_blight.jpg": add_late_blight_lesions(create_leaf_canvas(leaf_color=(40, 125, 35))),
        "potato_healthy.jpg": create_leaf_canvas(leaf_color=(40, 160, 50)),
        "corn_common_rust.jpg": add_rust_pustules(create_leaf_canvas(leaf_color=(60, 150, 45))),
        "apple_scab.jpg": add_apple_scab_lesions(create_leaf_canvas(leaf_color=(50, 140, 55)))
    }
    
    for filename, img in samples.items():
        filepath = assets_dir / filename
        img.save(filepath, quality=95)
        print(f"Generated sample leaf: {filepath}")
        
    # Also populate class folders in dataset/ for a realistic repository dataset inventory
    dataset_dir = base_dir / "dataset"
    for cls_name in ["Tomato___Early_blight", "Tomato___Late_blight", "Tomato___healthy",
                     "Potato___Early_blight", "Potato___Late_blight", "Potato___healthy",
                     "Corn___Common_rust", "Apple___Apple_scab"]:
        cls_folder = dataset_dir / cls_name
        cls_folder.mkdir(parents=True, exist_ok=True)
        # Place 2 sample images in each folder
        for i in range(1, 3):
            leaf_sample = create_leaf_canvas()
            leaf_sample.save(cls_folder / f"sample_{i}.jpg", quality=90)


if __name__ == "__main__":
    generate_all_samples()
