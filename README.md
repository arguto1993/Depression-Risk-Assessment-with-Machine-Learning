# Depression Risk Assessment with Machine Learning

## Objectives
This project aims to answer the following questions:
1. What are the main factors that contribute to depression risk in individuals?
2. How can a classification model be used to identify individuals at high risk of experiencing depression?

## Expected Results
1. Insights that answer the business questions above based on data analysis conducted.
2. A predictive model that can classify individuals into two categories: depressed (label 1) and not depressed (label 0), based on relevant factors. This model can be used by various educational institutions, companies, and organizations to provide greater attention to individuals at high risk of experiencing depression, so that intervention can be carried out earlier.
3. A website that demonstrates the model's ability to predict a person's depression risk.

## Dataset
- https://www.kaggle.com/datasets/hopesb/student-depression-dataset

## Application Website
- https://depression-risk-assessment.streamlit.app/

## Application Demo Video
- https://youtu.be/qTZRZB-TxGE

## Project Presentation Video
- https://youtu.be/DQWeNKIEiIo

## Project Structure

This project follows Streamlit best practices for code organization:

```
.
├── app.py
├── .streamlit/
│   └── config.toml
├── models/
│   ├── logistic_regression_model.pkl
│   ├── label_encoders.pkl
│   └── sleep_duration_mapping.pkl
├── pages/
│   ├── risk_assessment.py
│   ├── dashboard.py
│   └── about.py
├── utils/
│   ├── config.py
│   ├── data_loader.py
│   └── prediction.py
├── dataset/
├── documentation/
└── requirements.txt
```

## Running the Application

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open your browser and navigate to the provided local URL (typically http://localhost:8501)

---

*For the Bahasa Indonesia version of this README, please see [README.id.md](README.id.md)*
