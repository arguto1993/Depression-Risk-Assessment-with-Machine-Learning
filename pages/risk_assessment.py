"""
Risk Assessment page component for the Depression Risk Assessment application.
"""

import streamlit as st
import pandas as pd
from utils.config import (
    SLEEP_DURATION_OPTIONS,
    DIETARY_HABITS_OPTIONS,
    GENDER_OPTIONS
)
from utils.prediction import predict_depression, get_prediction_result_message


def render_risk_assessment_page():
    """Render the Risk Assessment page."""
    st.header("Depression Risk Assessment")
    
    # Collect user input
    name = st.text_input("Name")
    
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=0, max_value=100, step=1)
    with col2:
        gender = st.selectbox("Gender", GENDER_OPTIONS)
    
    col3, col4 = st.columns(2)
    with col3:
        profession = st.text_input("Profession")
    with col4:
        city = st.text_input("City of Domicile")
    
    # Prediction features
    academic_pressure = st.slider("Academic Pressure (5 = Most Pressure)", 0, 5, 0)
    work_pressure = st.slider("Work Pressure", 0, 5, 0)
    cgpa = st.number_input("CGPA (0.0 - 10.0)", min_value=0.0, max_value=10.0, step=0.1)
    study_satisfaction = st.slider("Study Satisfaction", 0, 10, 0)
    job_satisfaction = st.slider("Job Satisfaction", 0, 10, 0)
    
    sleep_duration = st.selectbox("Sleep Duration", SLEEP_DURATION_OPTIONS)
    
    family_history = st.radio("Family History of Mental Illness", ["No", "Yes"])
    feeling_depressed = st.radio("Are You Feeling Depressed?", ["No", "Yes"])
    
    dietary_habits = st.selectbox("Dietary Habits", DIETARY_HABITS_OPTIONS)
    
    suicidal_thoughts = st.radio("Have You Ever Had Suicidal Thoughts?", ["No", "Yes"])
    
    work_study_hours = st.number_input("Work/Study Hours per Day", min_value=0, max_value=12, step=1)
    financial_stress = st.slider("Financial Stress", 1, 5, 1)
    
    if st.button("Predict Depression Risk"):
        # Prepare data for prediction
        prediction_data = pd.DataFrame({
            'Have you ever had suicidal thoughts ?': [suicidal_thoughts],
            'Academic Pressure': [academic_pressure],
            'Financial Stress': [financial_stress],
            'Dietary Habits': [dietary_habits],
            'Study Satisfaction': [study_satisfaction],
            'Family History of Mental Illness': [family_history],
            'Sleep Duration': [sleep_duration],
            'Work/Study Hours': [work_study_hours],
            'Age': [age],
            'CGPA': [cgpa]
        })
        
        result = predict_depression(prediction_data)
        message, is_high_risk, confidence = get_prediction_result_message(result)
        
        # Display prediction
        if is_high_risk:
            st.error(message)
        else:
            st.success(message)
        st.write(confidence)
