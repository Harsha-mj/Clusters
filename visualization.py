# File: modules/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_elbow(inertia):
    fig, ax = plt.subplots()
    ax.plot(range(1, len(inertia) + 1), inertia, marker='o')
    ax.set_title('Elbow Method')
    ax.set_xlabel('Number of Clusters')
    ax.set_ylabel('Inertia')
    st.pyplot(fig)

def plot_clusters(data, labels, x_feature, y_feature):
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x=x_feature, y=y_feature, hue=labels, palette='Set2', ax=ax)
    ax.set_title(f'Cluster Visualization ({x_feature} vs {y_feature})')
    st.pyplot(fig)