import sklearn
import streamlit as st
import os
import joblib

# Load the pre-trained model
model = joblib.load('fraud_detection_pipeline.pkl')
if model:
    st.success('Model loaded successfully!')
else:
    st.error('Failed to load the model.')
print(sklearn.__version__)