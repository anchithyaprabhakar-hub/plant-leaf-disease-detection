"""
AgriVision AI - Streamlit Web Application
Interactive Dashboard for Deep Learning Plant Leaf Disease Detection
"""

import os
from pathlib import Path
import hashlib
from PIL import Image
import pandas as pd
import streamlit as st

from detection.disease_classifier import (
    load_classifier,
    predict_leaf_disease,
    get_device
)
from detection.disease_info import DISEASE_CLASSES, DISEASE_INFO, get_disease_info


# Page Configuration
st.set_page_state = getattr(st, "set_page_state", None)
st.set_page_config(
    page_title="AgriVision AI - Plant Leaf Disease Detection",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Root directory helper
BASE_DIR = Path(__file__).resolve().parent.parent
CSS_PATH = BASE_DIR / "ui" / "styles.css"
MODEL_PATH = BASE_DIR / "models" / "plant_disease_model.pth"
SAMPLE_DIR = BASE_DIR / "assets" / "sample_leaves"


def load_custom_css():
    """Inject custom glassmorphism styles."""
    if CSS_PATH.exists():
        with open(CSS_PATH, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


@st.cache_resource(show_spinner="Loading deep learning model weights...")
def get_cached_model():
    """Caches model in memory across Streamlit runs."""
    device = get_device()
    model = load_classifier(str(MODEL_PATH), device=device)
    return model, device


def render_header():
    """Renders the top branding hero container."""
    st.markdown(
        """
        <div class="hero-header">
            <div>
                <div class="hero-title">🌿 AgriVision AI</div>
                <p class="hero-subtitle">
                    Automated Agricultural Foliar Pathology & Deep Learning Diagnostic System
                </p>
            </div>
            <div>
                <span class="status-badge">
                    <span style="font-size: 1.2rem;">●</span> Deep CNN Active
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def display_diagnosis_report(result, image_pil):
    """Renders full diagnostic results including lesion analysis and remedies."""
    top_class = result["top_class"]
    confidence = result["top_confidence"]
    record = result["disease_record"]
    is_healthy = result["is_healthy"]
    
    # 1. Top Diagnosis Banner
    badge_class = "badge-healthy" if is_healthy else "badge-diseased"
    health_icon = "✅" if is_healthy else "⚠️"
    
    st.markdown(
        f"""
        <div class="glass-card">
            <div class="diagnosis-badge {badge_class}">
                {health_icon} {record['disease_name']} ({confidence:.1f}% Confidence)
            </div>
            <div>
                <span class="meta-pill">🌾 Crop: <strong>{record['crop']}</strong></span>
                <span class="meta-pill">🔬 Pathogen: <strong>{record['pathogen']}</strong></span>
                <span class="meta-pill">⚡ Severity: <strong>{record['severity']}</strong></span>
                <span class="meta-pill">🔍 Lesion Foliar Coverage: <strong>{result['lesion_percentage']}%</strong></span>
            </div>
            <p style="color: #cbd5e1; margin-top: 0.8rem; font-size: 0.95rem; line-height: 1.6;">
                {record['description']}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 2. Visual Diagnostics Columns
    st.markdown("<div class='section-title'>🖼️ Visual Foliar Inspection</div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.image(image_pil, caption="1. Input Leaf Image", use_container_width=True)
    with c2:
        st.image(result["annotated_image"], caption=f"2. Lesion Detections ({result['lesion_percentage']}% area)", use_container_width=True)
    with c3:
        st.image(result["heatmap_image"], caption="3. Pathogen Saliency Heatmap", use_container_width=True)
        
    # 3. Probabilistic Candidates Breakdown
    st.markdown("<div class='section-title'>📊 Candidate Predictions (Top-K Softmax)</div>", unsafe_allow_html=True)
    candidates_df = pd.DataFrame(result["candidates"])[["disease_name", "crop", "confidence", "severity"]]
    candidates_df.columns = ["Detected Condition", "Crop Host", "Confidence (%)", "Risk Level"]
    st.dataframe(candidates_df, use_container_width=True, hide_index=True)
    
    # Progress bar for top score
    st.progress(min(1.0, confidence / 100.0), text=f"Top-1 Diagnostic Certainty: {confidence:.1f}%")
    
    # 4. Comprehensive Pathology & Remedy Advisory
    st.markdown("<div class='section-title'>🛡️ Pathological Advisory & Management Protocol</div>", unsafe_allow_html=True)
    
    col_sym, col_org, col_chem = st.columns(3)
    
    with col_sym:
        st.markdown(
            """
            <div class="glass-card" style="height: 100%;">
                <h4 style="color: #6ee7b7; margin-bottom: 0.5rem;">🔍 Clinical Symptoms</h4>
                <ul style="color: #cbd5e1; font-size: 0.9rem; padding-left: 1.2rem;">
            """ + "".join([f"<li>{s}</li>" for s in record["symptoms"]]) + """
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with col_org:
        st.markdown(
            """
            <div class="glass-card remedy-box" style="height: 100%;">
                <h4 style="color: #34d399; margin-bottom: 0.5rem;">🌱 Organic & Cultural Controls</h4>
                <ul style="color: #cbd5e1; font-size: 0.9rem; padding-left: 1.2rem;">
            """ + "".join([f"<li>{r}</li>" for r in record["organic_remedies"]]) + """
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with col_chem:
        st.markdown(
            """
            <div class="glass-card remedy-box remedy-chemical" style="height: 100%;">
                <h4 style="color: #fbbf24; margin-bottom: 0.5rem;">🧪 Chemical & Fungicidal Treatment</h4>
                <ul style="color: #cbd5e1; font-size: 0.9rem; padding-left: 1.2rem;">
            """ + "".join([f"<li>{c}</li>" for c in record["chemical_control"]]) + """
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    # Prevention callout
    st.info(f"💡 **Preventive Field Strategy:** {record['prevention']}")


def run_app():
    """Main application loop."""
    load_custom_css()
    model, device = get_cached_model()
    
    # Sidebar
    with st.sidebar:
        st.markdown("### ⚙️ System Controls")
        st.markdown(f"**Inference Compute Device:** `{str(device).upper()}`")
        
        confidence_threshold = st.slider(
            "Confidence Alert Threshold (%)",
            min_value=30,
            max_value=95,
            value=50,
            step=5,
            help="Results below this threshold will display a low-confidence warning."
        )
        
        selected_crop_filter = st.selectbox(
            "Filter Target Crop Family",
            options=["All Crops", "Tomato", "Potato", "Corn", "Apple", "Grape", "Pepper"],
            index=0
        )
        
        st.markdown("---")
        st.markdown("### 📋 System Information")
        st.markdown(
            """
            - **Model Architecture:** PlantDiseaseCNN / ResNet Backbone
            - **Input Resolution:** 224 × 224 RGB
            - **Trained Classes:** 20 Agricultural Categories
            - **Backend Engine:** PyTorch & OpenCV
            - **Framework:** Streamlit Native
            """
        )
        st.markdown("---")
        st.caption("AgriVision AI Academic Project Demonstration")

    render_header()
    
    tabs = st.tabs([
        "📤 Upload & Diagnose",
        "📷 Live Camera Capture",
        "🧪 Instant Test Samples",
        "📚 Pathology Catalog",
        "🧠 Neural Architecture"
    ])
    
    # ---------------- TAB 1: UPLOAD & DIAGNOSE ----------------
    with tabs[0]:
        st.markdown("##### Upload a Leaf Photo for Immediate Analysis")
        uploaded_file = st.file_uploader(
            "Select a leaf photo (JPG, JPEG, PNG)",
            type=["jpg", "jpeg", "png"],
            key="file_uploader"
        )
        
        if uploaded_file is not None:
            image_pil = Image.open(uploaded_file).convert("RGB")
            
            c_preview, c_action = st.columns([1, 2])
            with c_preview:
                st.image(image_pil, caption="Uploaded Leaf Preview", use_container_width=True)
                
            with c_action:
                st.markdown(
                    """
                    <div class="glass-card">
                        <h4>Ready for Foliar Diagnosis</h4>
                        <p style="color: #94a3b8; font-size: 0.9rem;">
                            Click below to execute the 5-stage convolutional pipeline:
                            tensor normalization, deep feature extraction, softmax classification,
                            and necrotic lesion segmentation.
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                analyze_btn = st.button("🚀 Analyze Plant Leaf", type="primary", use_container_width=True)
                
            if analyze_btn:
                with st.spinner("Analyzing foliar patterns and computing disease probability..."):
                    result = predict_leaf_disease(image_pil, model, device=device)
                    display_diagnosis_report(result, image_pil)
                    
                    if result["top_confidence"] < confidence_threshold:
                        st.warning(
                            f"⚠️ Diagnosis confidence ({result['top_confidence']}%) is below your configured threshold "
                            f"({confidence_threshold}%). Inspect leaf symptoms or capture higher resolution under uniform light."
                        )

    # ---------------- TAB 2: LIVE CAMERA CAPTURE ----------------
    with tabs[1]:
        st.markdown("##### Capture Leaf Directly with Device Camera")
        camera_img = st.camera_input("Point camera at suspect leaf against neutral background")
        
        if camera_img is not None:
            image_pil = Image.open(camera_img).convert("RGB")
            with st.spinner("Processing camera frame through deep learning pipeline..."):
                result = predict_leaf_disease(image_pil, model, device=device)
                display_diagnosis_report(result, image_pil)

    # ---------------- TAB 3: INSTANT TEST SAMPLES ----------------
    with tabs[2]:
        st.markdown("##### 1-Click Verification using Included Botanical Test Samples")
        st.write("Click any sample card to test the end-to-end pipeline instantly:")
        
        samples_list = [
            ("Tomato Early Blight", "tomato_early_blight.jpg", "Concentric target spots on tomato"),
            ("Tomato Late Blight", "tomato_late_blight.jpg", "Water-soaked foliar rot"),
            ("Tomato Healthy", "tomato_healthy.jpg", "Vibrant disease-free foliage"),
            ("Potato Early Blight", "potato_early_blight.jpg", "Target lesions on solanum leaves"),
            ("Potato Late Blight", "potato_late_blight.jpg", "Aggressive necrotic blight lesions"),
            ("Corn Common Rust", "corn_common_rust.jpg", "Cinnamon-brown rust pustules"),
            ("Apple Scab", "apple_scab.jpg", "Olive-brown velvety scab lesions"),
            ("Potato Healthy", "potato_healthy.jpg", "Clean potato foliage")
        ]
        
        cols = st.columns(4)
        for i, (label, filename, desc) in enumerate(samples_list):
            sample_path = SAMPLE_DIR / filename
            col_target = cols[i % 4]
            with col_target:
                if sample_path.exists():
                    img = Image.open(sample_path)
                    st.image(img, use_container_width=True)
                    if st.button(f"Diagnose {label}", key=f"btn_sample_{i}", use_container_width=True):
                        st.session_state["active_sample"] = filename
                        
        if "active_sample" in st.session_state:
            active_file = SAMPLE_DIR / st.session_state["active_sample"]
            if active_file.exists():
                st.markdown("---")
                st.markdown(f"### 🔬 Detailed Analysis for `{st.session_state['active_sample']}`")
                sample_img = Image.open(active_file)
                result = predict_leaf_disease(sample_img, model, device=device)
                display_diagnosis_report(result, sample_img)

    # ---------------- TAB 4: PATHOLOGY CATALOG ----------------
    with tabs[3]:
        st.markdown("##### Searchable Plant Pathology and Remedy Reference")
        search_query = st.text_input("🔍 Search by crop name, disease, or pathogen:", "")
        
        filtered_classes = DISEASE_CLASSES
        if search_query:
            filtered_classes = [
                c for c in DISEASE_CLASSES
                if search_query.lower() in c.lower() or
                   search_query.lower() in DISEASE_INFO.get(c, {}).get("disease_name", "").lower() or
                   search_query.lower() in DISEASE_INFO.get(c, {}).get("crop", "").lower()
            ]
            
        for cls_name in filtered_classes:
            info = get_disease_info(cls_name)
            with st.expander(f"🌿 {info['crop']} — {info['disease_name']} ({info['severity']})"):
                st.write(f"**Pathogen:** {info['pathogen']}")
                st.write(f"**Description:** {info['description']}")
                st.write("**Symptoms:**")
                for s in info["symptoms"]:
                    st.write(f"- {s}")
                st.write("**Organic & Cultural Remedies:**")
                for r in info["organic_remedies"]:
                    st.write(f"- {r}")
                st.write("**Chemical Control:**")
                for c in info["chemical_control"]:
                    st.write(f"- {c}")
                st.write(f"**Prevention:** {info['prevention']}")

    # ---------------- TAB 5: NEURAL ARCHITECTURE ----------------
    with tabs[4]:
        st.markdown("##### Neural Network Topology & Training Pipeline")
        st.markdown(
            """
            The **PlantDiseaseCNN** architecture employs a 5-stage hierarchical feature extraction pipeline:
            
            ```
            Input Image [3 x 224 x 224]
              │
              ├── ConvBlock 1: Conv2d(3->32, 3x3) + BatchNorm + ReLU + MaxPool(2x2) + Dropout(0.10)   --> [32 x 112 x 112]
              ├── ConvBlock 2: Conv2d(32->64, 3x3) + BatchNorm + ReLU + MaxPool(2x2) + Dropout(0.15)  --> [64 x 56 x 56]
              ├── ConvBlock 3: Conv2d(64->128, 3x3) + BatchNorm + ReLU + MaxPool(2x2) + Dropout(0.20) --> [128 x 28 x 28]
              ├── ConvBlock 4: Conv2d(128->256, 3x3) + BatchNorm + ReLU + MaxPool(2x2) + Dropout(0.25) -> [256 x 14 x 14]
              ├── ConvBlock 5: Conv2d(256->512, 3x3) + BatchNorm + ReLU + MaxPool(2x2) + Dropout(0.30) -> [512 x 7 x 7]
              │
              ├── AdaptiveAvgPool2d((1, 1))                                                          --> [512 x 1 x 1]
              │
              └── Dense Head: Flatten -> Linear(512->256) -> BatchNorm1d -> ReLU -> Dropout(0.40) -> Linear(256->20 Classes)
            ```
            
            ##### Key Highlights:
            - **Batch Normalization** after each convolution ensures fast convergence and stabilizes gradients across high dynamic ranges of natural leaf lighting.
            - **Progressive Spatial Downsampling** preserves fine vein textures in shallow layers while building invariant representations of necrotic spots in deeper blocks.
            - **Regularization Pipeline:** Staged spatial dropout (0.10 -> 0.30) and fully-connected dropout (0.40) strictly mitigate overfitting on lab-collected backgrounds.
            - **Softmax Calibration:** Evaluates posterior probability distributions across 20 distinct host-pathogen pairs.
            """
        )


if __name__ == "__main__":
    run_app()
