import streamlit as st
from utils.config import PAGE_TITLE, APP_TITLE
from pages import render_risk_assessment_page, render_dashboard_page, render_about_page


def main():
    # Configure the page
    st.set_page_config(
        page_title=PAGE_TITLE,
        layout="wide",
        # page_icon="favicon.png",
    )

    # App title
    st.title(APP_TITLE)

    # Create tabs for different sections
    tab1, tab2, tab3 = st.tabs(["Risk Assessment", "Dashboard", "About"])

    # Render each tab's content
    with tab1:
        render_risk_assessment_page()

    with tab2:
        render_dashboard_page()

    with tab3:
        render_about_page()


if __name__ == "__main__":
    main()
