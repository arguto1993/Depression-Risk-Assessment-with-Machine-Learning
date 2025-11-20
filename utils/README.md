# Utils Module

This directory contains utility modules for the Depression Risk Assessment application.

## Modules

### `config.py`
Contains all configuration constants and settings for the application including:
- Model file paths
- Feature configurations
- UI constants
- External links

### `data_loader.py`
Handles loading and caching of model artifacts:
- `load_model()`: Loads the trained logistic regression model
- `load_label_encoders()`: Loads the label encoders for categorical features
- `load_sleep_duration_mapping()`: Loads the sleep duration mapping dictionary

All functions use Streamlit's `@st.cache_resource` decorator for efficient caching.

### `prediction.py`
Contains the prediction logic:
- `predict_depression(new_data)`: Makes predictions on input data
- `get_prediction_result_message(prediction_result)`: Formats prediction results for display

## Usage

```python
from utils import predict_depression, load_model
from utils.config import PAGE_TITLE

# Use configuration constants
st.set_page_config(page_title=PAGE_TITLE)

# Make predictions
result = predict_depression(input_data)
```
