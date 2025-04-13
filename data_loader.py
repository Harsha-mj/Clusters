# File: modules/data_loader.py
import pandas as pd
import logging

def load_sample_data():
    try:
        data = pd.DataFrame({
            'Age': [],
            'Annual Income (k$)': [],
            'Spending Score (1-100)': []
        })
        logging.info("Initialized empty sample data")
        return data
    except Exception as e:
        logging.error("Error initializing sample data: %s", e)
        raise


# File: modules/data_cleaning.py
def clean_data(data):
    try:
        data.dropna(inplace=True)
        logging.info("Null values dropped")
        return data
    except Exception as e:
        logging.error("Error in data cleaning: %s", e)
        raise
