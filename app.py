import streamlit as st
import joblib
import numpy as np
import logging

# Set up basic logging to console (stdout)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the model
model_path = "kmeans_model.pkl"
try:
    model = joblib.load(model_path)
    logger.info("✅ Model loaded successfully from %s", model_path)
except Exception as e:
    logger.error("❌ Error loading model: %s", e)
    st.error("Failed to load the model.")
    st.stop()

# Streamlit UI
st.title("🛍️ Customer Segment Predictor")
st.markdown("Enter your details to find out which customer segment you belong to based on clustering!")

# User inputs
age = st.number_input("Age", min_value=1, max_value=100, value=25)
income = st.number_input("Annual Income (in $1000s)", min_value=1, max_value=200, value=50)
score = st.number_input("Spending Score (1-100)", min_value=1, max_value=100, value=50)

# Predict button
if st.button("Predict Segment"):
    try:
        user_data = np.array([[age, income, score]])
        prediction = model.predict(user_data)
        logger.info("Prediction successful. Input: %s, Segment: %s", user_data.tolist(), prediction[0])
        st.success(f"🎯 You belong to customer segment: {prediction[0]}")
    except Exception as e:
        logger.exception("Prediction failed")
        st.error(f"Prediction failed: {e}")
