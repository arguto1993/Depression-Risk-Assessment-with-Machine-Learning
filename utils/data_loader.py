import pickle
import streamlit as st
from utils.config import MODEL_PATH, LABEL_ENCODERS_PATH, SLEEP_DURATION_MAPPING_PATH


@st.cache_resource
def load_model():
    """
    Load the trained logistic regression model.

    Returns:
        The trained model object.
    """
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


@st.cache_resource
def load_label_encoders():
    """
    Load the label encoders for categorical features.

    Returns:
        Dictionary of label encoders.
    """
    with open(LABEL_ENCODERS_PATH, "rb") as f:
        return pickle.load(f)


@st.cache_resource
def load_sleep_duration_mapping():
    """
    Load the sleep duration mapping dictionary.

    Returns:
        Dictionary mapping sleep duration strings to numeric values.
    """
    with open(SLEEP_DURATION_MAPPING_PATH, "rb") as f:
        return pickle.load(f)
