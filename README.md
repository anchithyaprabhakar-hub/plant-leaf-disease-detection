# 🌿 Plant Leaf Disease Detection System Using Deep Learning

An end-to-end computer-vision and deep learning application for the rapid automated diagnosis of plant foliar diseases across major agricultural crops (Tomato, Potato, Corn, Apple, Grape, Pepper). The system combines deep Convolutional Neural Networks (CNN) with adaptive lesion segmentation and an interactive Streamlit graphical interface to deliver real-time diagnostic confidence scores, clinical symptom summaries, and tailored organic and chemical treatment recommendations.

---

## 📌 Project Overview

Plant diseases represent a critical threat to global agricultural food security, reducing annual crop yields by an estimated 20% to 40%. Traditional manual visual inspection requires rare phytopathological expertise and is often too slow to prevent widespread field epidemics. 

This project delivers an interactive, automated diagnostics pipeline that:
1. **Acquires Foliar Imagery:** Supports high-resolution file uploads (JPG, PNG) and real-time device camera snapshots.
2. **Standardizes & Preprocesses:** Performs tensor conversion, channel verification, bicubic resizing (224 × 224 pixels), and ImageNet statistical normalization.
3. **Extracts Deep Hierarchical Features:** Employs a 5-stage convolutional feature extractor (`PlantDiseaseCNN`) with Batch Normalization, Dropout, and Adaptive Average Pooling.
4. **Calibrates Multi-Class Probabilities:** Computes calibrated Softmax posterior distributions over 20 distinct crop-pathogen categories.
5. **Localizes Lesions:** Implements computer-vision lesion boundary extraction and attention saliency heatmaps to visually isolate diseased leaf tissue.
6. **Recommends Interventions:** Automatically pairs every detected disease with immediate biological, cultural, and chemical treatment guidelines.

---

## 🏗️ Repository Architecture

```
plant-leaf-disease-detection/
├── app.py                         # Root application launcher
├── README.md                      # Repository documentation and run guide
├── requirements.txt               # Pinned Python package dependencies
├── create_sample_assets.py        # Utility generating sample leaves & datasets
├── assets/
│   └── sample_leaves/             # Botanical test leaves for instant 1-click verification
│       ├── tomato_early_blight.jpg
│       ├── tomato_late_blight.jpg
│       ├── tomato_healthy.jpg
│       ├── potato_early_blight.jpg
│       ├── potato_late_blight.jpg
│       ├── potato_healthy.jpg
│       ├── corn_common_rust.jpg
│       └── apple_scab.jpg
├── dataset/                       # Class-partitioned dataset folders
│   ├── Apple___Apple_scab/
│   ├── Corn___Common_rust/
│   ├── Potato___Early_blight/
│   ├── Potato___Late_blight/
│   ├── Potato___healthy/
│   ├── Tomato___Early_blight/
│   ├── Tomato___Late_blight/
│   └── Tomato___healthy/
├── detection/
│   ├── disease_classifier.py      # Core inference engine (tensor pipeline, lesion segmentation)
│   └── disease_info.py            # Comprehensive plant pathology & remedy database
├── models/
│   ├── plant_disease_model.pth    # Serialized PyTorch deep learning weights
│   └── model_builder.py           # Deep CNN & MobileNetV2 architecture definitions
├── ui/
│   ├── app.py                     # Streamlit multi-tab dashboard implementation
│   └── styles.css                 # Custom emerald glassmorphism styling
└── PROJECT_REPORT.md              # Full 25-page academic project report
```

---

## 🛠️ Tools & Technologies Used

| Category | Technology | Role in Repository |
| :--- | :--- | :--- |
| **Language** | Python 3.10 – 3.14 | Core application, inference pipeline, and data orchestration |
| **Deep Learning** | PyTorch / TorchVision | Deep convolutional network construction, weight management, and tensor forward pass |
| **Computer Vision** | OpenCV (`cv2`) | Color space transformation (HSV/Lab), morphological filtering, and lesion boundary contours |
| **Numerical Processing** | NumPy | Matrix transformations, tensor manipulation, and probability array slicing |
| **Image Handling** | Pillow (PIL) | Multi-format image ingestion, conversion, and canvas manipulation |
| **Web Interface** | Streamlit | Responsive, real-time dashboard rendering, caching, and camera stream integration |
| **Styling** | Vanilla CSS (`ui/styles.css`) | Glassmorphic visual presentation, theme tokens, badges, and layout polish |

---

## ⚡ Installation & Execution Guide

### 1. Clone or Navigate to the Repository
```bash
cd /Users/anchithyaprabhakar/.gemini/antigravity-ide/scratch/plant-leaf-disease-detection
```

### 2. Create and Activate Virtual Environment
```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows PowerShell
# python -m venv .venv
# .venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Launch the Streamlit Application
```bash
streamlit run app.py
```
The browser will automatically open at `http://localhost:8501`.

---

## 🌿 Supported Crops and Foliar Diseases

The system detects and diagnoses 20 agricultural disease conditions across 6 host crop families:

1. **Apple:** Apple Scab (*Venturia inaequalis*), Black Rot (*Botryosphaeria obtusa*), Cedar Apple Rust (*Gymnosporangium*), Healthy.
2. **Corn / Maize:** Common Rust (*Puccinia sorghi*), Northern Leaf Blight (*Exserohilum turcicum*), Healthy.
3. **Grape:** Black Rot (*Guignardia bidwellii*), Esca Black Measles (*Complex*), Healthy.
4. **Bell Pepper:** Bacterial Spot (*Xanthomonas campestris*), Healthy.
5. **Potato:** Early Blight (*Alternaria solani*), Late Blight (*Phytophthora infestans*), Healthy.
6. **Tomato:** Bacterial Spot, Early Blight (*Alternaria linariae*), Late Blight (*Phytophthora infestans*), Leaf Mold (*Passalora fulva*), Healthy.

---

## 🔬 Scientific Disclaimer
This software demonstration is intended for educational, academic, and decision-support purposes. While deep learning provides powerful visual pattern recognition, final agrochemical application decisions should be cross-verified with qualified local agricultural extension officers or physical laboratory culture tests.
