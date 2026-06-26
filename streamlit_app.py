# This file serves as the entry point for Streamlit Cloud deployment
# It imports and runs the main application from 1_Home.py

import streamlit as st
import importlib.util
import sys
from pathlib import Path

# Load 1_Home.py as the main module
home_path = Path(__file__).parent / "1_Home.py"
spec = importlib.util.spec_from_file_location("home", home_path)
home_module = importlib.util.module_from_spec(spec)
sys.modules["home"] = home_module
spec.loader.exec_module(home_module)
