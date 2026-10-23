"""
Plant Leaf Disease Detection System Launcher
Root entry point importing and executing the Streamlit application module.
"""

import sys
from pathlib import Path

# Ensure root directory is accessible on Python module search path
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from ui.app import run_app

if __name__ == "__main__":
    run_app()
