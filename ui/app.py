"""
AgriVision AI - Streamlit Web Application
Streamlined Deep Learning Diagnostic Dashboard for Plant Leaf Disease Detection
"""

import os
from pathlib import Path
from PIL import Image
import pandas as pd
import streamlit as st

from detection.disease_classifier import (
    load_classifier,
    predict_leaf_disease,
    get_device
)


# Page Configuration
st.set_page_config(
    page_title="AgriVision AI - Plant Leaf Disease Detection",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Root directory helper
BASE_DIR = Path(__file__).resolve().parent.parent
CSS_PATH = BASE_DIR / "ui" / "styles.css"


def load_custom_css():
    """Inject custom glassmorphism styles."""
    if CSS_PATH.exists():
        with open(CSS_PATH, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


@st.cache_resource(show_spinner="Loading deep learning model weights...")
def get_cached_model():
    """Caches model in memory across Streamlit runs."""
    device = get_device()
    bundle = load_classifier(device=device)
    return bundle, device


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
                    <span style="font-size: 1.2rem;">●</span> Deep Neural Network Active
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
    is_confident = result.get("is_confident", True)
    crop_filter = result.get("crop_filter")
    threshold = result.get("confidence_threshold", 50.0)

    # 1. Top Diagnosis Banner or Low-Confidence Warning
    if not is_confident:
        st.markdown(
            f"""
            <div class="glass-card" style="border-left: 4px solid #f59e0b;">
                <div style="font-size: 1.15rem; font-weight: 700; color: #fbbf24; margin-bottom: 0.4rem;">
                    ⚠️ Low Diagnostic Certainty ({confidence:.1f}% vs {threshold:.0f}% required)
                </div>
                <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6; margin-bottom: 0.6rem;">
                    The foliage input does not match any cataloged disease pattern with high statistical certainty.
                    Tentative closest match is <strong>{record['disease_name']} ({record['crop']})</strong>.
                </p>
                <div style="background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.25); padding: 0.75rem 1rem; border-radius: 8px; color: #fde68a; font-size: 0.88rem;">
                    <strong>🔍 Diagnostic Guidance:</strong><br>
                    • <strong>Frame Framing:</strong> Position the camera closer so the suspected leaf covers at least 70% of the viewport.<br>
                    • <strong>Lighting & Background:</strong> Aim for diffused natural daylight against a neutral, uncluttered background.<br>
                    • <strong>Crop Targeting:</strong> If you know the plant species (e.g., Tomato), select it in the <strong>Filter Target Crop Family</strong> sidebar dropdown to focus analysis on that specific botanical family.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        badge_class = "badge-healthy" if is_healthy else "badge-diseased"
        health_icon = "✅" if is_healthy else "⚠️"
        filter_tag = f'<span class="meta-pill" style="border-color: #38bdf8; color: #7dd3fc;">🎯 Crop Filter: <strong>{crop_filter}</strong></span>' if crop_filter and crop_filter != "All Crops" else ""

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
                    {filter_tag}
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
        st.image(image_pil, caption="1. Input Foliage Image", use_container_width=True)
    with c2:
        st.image(result["annotated_image"], caption=f"2. OpenCV Lesion Detections ({result['lesion_percentage']}% foliar area)", use_container_width=True)
    with c3:
        st.image(result["heatmap_image"], caption="3. Pathogen Saliency Heatmap", use_container_width=True)

    # 3. Probabilistic Candidates Breakdown
    st.markdown("<div class='section-title'>📊 Candidate Predictions (Top-K Softmax)</div>", unsafe_allow_html=True)
    candidates_df = pd.DataFrame(result["candidates"])[["disease_name", "crop", "confidence", "severity"]]
    candidates_df.columns = ["Detected Condition", "Crop Host", "Confidence (%)", "Risk Level"]
    st.dataframe(candidates_df, use_container_width=True, hide_index=True)

    # Progress bar for top score
    st.progress(min(1.0, confidence / 100.0), text=f"Diagnostic Certainty: {confidence:.1f}%")

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
    model_bundle, device = get_cached_model()

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
            help="Results below this threshold will display an inconclusive/low-confidence warning."
        )

        selected_crop_filter = st.selectbox(
            "Filter Target Crop Family",
            options=["All Crops", "Tomato", "Potato", "Corn", "Apple", "Grape", "Pepper", "Peach", "Cherry", "Strawberry", "Squash"],
            index=0,
            help="Optionally restrict candidate classification to a specific agricultural crop family."
        )

        if selected_crop_filter != "All Crops":
            st.success(f"🎯 Target Filter Active: **{selected_crop_filter}**")

        st.markdown("---")
        st.markdown("### 📋 System Information")
        st.markdown(
            """
            - **Model Architecture:** MobileNetV2 Deep CNN
            - **Input Resolution:** 224 × 224 RGB
            - **Trained Classes:** 38 Agricultural Foliar Classes
            - **Backend Engine:** PyTorch & OpenCV
            - **Pre-trained Benchmark:** PlantVillage Standard
            """
        )
        st.markdown("---")
        st.caption("AgriVision AI Foliar Pathology Diagnostic System")

    render_header()

    tabs = st.tabs([
        "📤 Upload Leaf Photo",
        "📷 Live Camera Capture"
    ])

    # ---------------- TAB 1: UPLOAD LEAF PHOTO ----------------
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
                    f"""
                    <div class="glass-card">
                        <h4>Ready for Foliar Diagnosis</h4>
                        <p style="color: #94a3b8; font-size: 0.9rem;">
                            Click below to execute the deep neural inference pipeline:
                            tensor normalization, deep feature extraction, softmax classification,
                            and necrotic lesion segmentation.
                        </p>
                        <p style="color: #38bdf8; font-size: 0.85rem; margin: 0;">
                            Target Filter: <strong>{selected_crop_filter}</strong> | Alert Threshold: <strong>{confidence_threshold}%</strong>
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                analyze_btn = st.button("🚀 Analyze Plant Leaf", type="primary", use_container_width=True)

            if analyze_btn:
                with st.spinner("Analyzing foliar patterns and computing disease probability..."):
                    result = predict_leaf_disease(
                        image_pil,
                        model_bundle,
                        device=device,
                        crop_filter=selected_crop_filter,
                        confidence_threshold=confidence_threshold
                    )
                    display_diagnosis_report(result, image_pil)

    # ---------------- TAB 2: LIVE CAMERA CAPTURE ----------------
    with tabs[1]:
        st.markdown("##### Capture Leaf Directly with Device Camera")
        st.info("💡 **Tip:** Hold the camera steady and position the suspect leaf in the center of the frame against a neutral background.")
        camera_img = st.camera_input("Point camera at suspect leaf against neutral background")

        if camera_img is not None:
            image_pil = Image.open(camera_img).convert("RGB")
            with st.spinner("Processing camera frame through deep learning pipeline..."):
                result = predict_leaf_disease(
                    image_pil,
                    model_bundle,
                    device=device,
                    crop_filter=selected_crop_filter,
                    confidence_threshold=confidence_threshold
                )
                display_diagnosis_report(result, image_pil)


if __name__ == "__main__":
    run_app()
