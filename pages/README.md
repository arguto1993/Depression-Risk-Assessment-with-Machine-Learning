# Pages Module

This directory contains page components for the Depression Risk Assessment application.

## Page Components

### `risk_assessment.py`
The main risk assessment page where users can:
- Enter personal information (name, age, gender, profession, city)
- Provide depression risk factors (academic pressure, sleep duration, etc.)
- Get a depression risk prediction with confidence score

**Function:** `render_risk_assessment_page()`

### `dashboard.py`
The dashboard page that links to the Looker Studio dashboard for viewing depression statistics.

**Function:** `render_dashboard_page()`

### `about.py`
The about page containing:
- Project disclaimer and warnings
- Project details and objectives
- Links to project resources

**Function:** `render_about_page()`

## Usage

Each page module exports a single render function that can be called within a Streamlit tab or page:

```python
from pages import render_risk_assessment_page, render_dashboard_page, render_about_page

# In main app
with tab1:
    render_risk_assessment_page()

with tab2:
    render_dashboard_page()

with tab3:
    render_about_page()
```

## Design Pattern

Each page component:
- Is self-contained and focuses on a single responsibility
- Uses utilities from the `utils` module
- Returns None (renders directly to Streamlit)
- Follows consistent naming: `render_<page_name>_page()`
