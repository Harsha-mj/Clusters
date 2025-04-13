# File: modules/clustering.py
from sklearn.cluster import KMeans
import numpy as np

def get_elbow_values(data, max_k=10):
    try:
        inertia = []
        for k in range(1, max_k + 1):
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(data)
            inertia.append(kmeans.inertia_)
        logging.info("Elbow method computed")
        return inertia
    except Exception as e:
        logging.error("Error computing elbow values: %s", e)
        raise

def apply_kmeans(data, n_clusters):
    try:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        labels = kmeans.fit_predict(data)
        logging.info("KMeans clustering applied with %d clusters", n_clusters)
        return labels, kmeans
    except Exception as e:
        logging.error("Error applying KMeans: %s", e)
        raise