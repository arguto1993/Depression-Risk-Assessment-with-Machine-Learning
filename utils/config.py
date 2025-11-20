"""
Configuration constants for the Depression Risk Assessment application.
"""

# Model file paths
MODEL_PATH = "models/logistic_regression_model.pkl"
LABEL_ENCODERS_PATH = "models/label_encoders.pkl"
SLEEP_DURATION_MAPPING_PATH = "models/sleep_duration_mapping.pkl"

# Feature configuration
SELECTED_FEATURES = [
    'Have you ever had suicidal thoughts ?',
    'Academic Pressure',
    'Financial Stress',
    'Dietary Habits',
    'Study Satisfaction',
    'Family History of Mental Illness',
    'Sleep Duration',
    'Work/Study Hours',
    'Age',
    'CGPA'
]

CATEGORICAL_FEATURES = [
    'Have you ever had suicidal thoughts ?',
    'Dietary Habits',
    'Family History of Mental Illness'
]

# UI configuration
PAGE_TITLE = "Depression Risk Assessment"
APP_TITLE = "Depression Risk Assessment With Machine Learning"

# Sleep duration options
SLEEP_DURATION_OPTIONS = [
    "Less than 5 hours",
    "5-6 hours",
    "7-8 hours",
    "More than 8 hours"
]

# Dietary habits options
DIETARY_HABITS_OPTIONS = [
    "Healthy",
    "Moderate",
    "Unhealthy",
    "Others"
]

# Gender options
GENDER_OPTIONS = ["", "Male", "Female", "Other"]

# Links
DASHBOARD_LINK = "https://lookerstudio.google.com/reporting/8fee9fb4-8d82-4460-9943-61726e9887ad"
PROJECT_BRIEF_LINK = "https://drive.google.com/file/d/1umXcOXX_fML-y_UdQEZ2eGLYNk7C_VZi/view?usp=sharing"
GITHUB_REPO_LINK = "https://github.com/arguto1993/depression-risk-classification/tree/main"
DATASET_LINK = "https://www.kaggle.com/datasets/hopesb/student-depression-dataset"
