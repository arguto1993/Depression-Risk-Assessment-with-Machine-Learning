import pandas as pd
from utils.config import SELECTED_FEATURES, CATEGORICAL_FEATURES
from utils.data_loader import (
    load_model,
    load_label_encoders,
    load_sleep_duration_mapping,
)


def predict_depression(new_data):
    """
    Predict depression risk for a given input.

    Args:
        new_data: pandas DataFrame containing the input features.

    Returns:
        Dictionary with 'prediction' (class label) and 'probability' (confidence score).
    """
    model = load_model()
    label_encoders = load_label_encoders()
    sleep_duration_mapping = load_sleep_duration_mapping()

    # Copy data to avoid modifying the original
    processed_data = new_data.copy()

    # Encode categorical features safely
    for feature in CATEGORICAL_FEATURES:
        if feature in processed_data:
            processed_data[feature] = label_encoders[feature].transform(
                [processed_data[feature]]
            )[0]

    # Map Sleep Duration
    processed_data["Sleep Duration"] = (
        processed_data["Sleep Duration"]
        .map(sleep_duration_mapping)
        .fillna(-1)
        .astype(int)
    )

    # Ensure input follows training feature order
    input_data = pd.DataFrame(
        [{feature: processed_data[feature] for feature in SELECTED_FEATURES}]
    )

    # Debug
    print("Expected Features:", model.feature_names_in_)
    print("Current Features:", input_data.columns.tolist())

    # Predict
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    return {
        "prediction": prediction[0],  # Class label
        "probability": prediction_proba[0].max(),  # Confidence score
    }


def get_prediction_result_message(prediction_result):
    """
    Get a formatted message for the prediction result.

    Args:
        prediction_result: Dictionary containing prediction and probability.

    Returns:
        Tuple of (message, is_high_risk) where is_high_risk is a boolean.
    """
    prediction = prediction_result["prediction"]
    probability = prediction_result["probability"]

    if prediction == 1:
        message = "Higher Risk of Depression Detected"
        is_high_risk = True
    else:
        message = "Lower Risk of Depression Detected"
        is_high_risk = False

    confidence = f"Confidence: {probability * 100:.2f}%"

    return message, is_high_risk, confidence
