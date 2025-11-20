"""
Dashboard page component for the Depression Risk Assessment application.
"""

import streamlit as st
from utils.config import DASHBOARD_LINK


def render_dashboard_page():
    """Render the Dashboard page."""
    st.header("Student Depression Dashboard")
    st.markdown(f"[View Dashboard on Looker Studio]({DASHBOARD_LINK})")
