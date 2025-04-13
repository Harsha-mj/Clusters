# File: app.py
import streamlit as st
import logging
import pandas as pd
from data_cleaning import clean_data
from clustering import get_elbow_values, apply_kmeans
from visualization import plot_elbow, plot_clusters
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

logging.basicConfig(filename='logs/app.log', level=logging.INFO)

st.title("Mall Customer Clustering App")

st.markdown("Enter Customer Features (Age, Annual Income and Spending Score)")

with st.form("input_form"):
    age_list = st.text_area("Enter Age values, separated by commas")
    income_list = st.text_area("Enter Annual Income (k$) values, separated by commas")
    score_list = st.text_area("Enter Spending Score (1-100) values, separated by commas")
    submitted = st.form_submit_button("Run Clustering")

if submitted:
    try:
        age_values = [float(x.strip()) for x in age_list.split(',') if x.strip()]
        income_values = [float(x.strip()) for x in income_list.split(',') if x.strip()]
        score_values = [float(x.strip()) for x in score_list.split(',') if x.strip()]

        if not (len(age_values) == len(income_values) == len(score_values)):
            st.error("The number of Age, Income, and Score values must match.")
        else:
            data = pd.DataFrame({
                'Age': age_values,
                'Annual Income (k$)': income_values,
                'Spending Score (1-100)': score_values
            })

            st.write("Cleaned Data", data)

            data = clean_data(data)
            inertia = get_elbow_values(data)
            plot_elbow(inertia)

            k = st.slider("Select number of clusters", 2, 10, 5)
            labels, model = apply_kmeans(data, k)

            x_feature = st.selectbox("Select X-axis for cluster plot", data.columns)
            y_feature = st.selectbox("Select Y-axis for cluster plot", data.columns, index=2)

            plot_clusters(data, labels, x_feature, y_feature)

    except Exception as e:
        st.error(f"Error: {e}")
