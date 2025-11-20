"""
About page component for the Depression Risk Assessment application.
"""

import streamlit as st
from utils.config import DATASET_LINK, PROJECT_BRIEF_LINK, GITHUB_REPO_LINK


def render_about_page():
    """Render the About page."""
    st.header("About This Project")
    st.markdown(f"""
    **Disclaimer:** This is a machine learning demo for depression risk assessment. The model is trained on a dataset of [student-depression-dataset]({DATASET_LINK}) and may not be suitable for all individuals.
    - **Not a Medical Diagnosis:** This tool CANNOT replace professional medical advice.
    - If you're experiencing depression or mental health challenges, please consult a healthcare professional.

    **Project Details:**
    - Developed by 4 Data Science students from Dicoding Indonesia Bootcamp 2024-2025
    - Purpose: Demonstrate machine learning application in mental health screening especially for student depression risk assessment.

    **Remember:** Your mental health is important. Seek professional help if needed.
    """
    )
    
    st.markdown(f"[Project Brief (ID)]({PROJECT_BRIEF_LINK})")
    st.markdown(f"[Github Repository]({GITHUB_REPO_LINK})")
