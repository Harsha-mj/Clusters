# Clusters
# File: README.md
# Mall Customer Segmentation (Unsupervised Clustering)
This app has been built using Streamlit and deployed with Streamlit community cloud
[Visit the app here](https://clusters-vvdqtz8fvnwggpfw3bdzmx.streamlit.app/)

This project uses KMeans clustering on mall customer data to segment customers based on features like Age, Annual Income, and Spending Score.

## Folder Structure
- `modules/`: Contains modular Python scripts for data loading, cleaning, clustering, and visualization.
- `app.py`: Streamlit web app.
- `logs/`: Contains logs for debugging.
- `data/`: (Optional) Include reference datasets.

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Dependencies
See `requirements.txt` for full list.

## Deployment
The app can be deployed on Streamlit Cloud. Ensure your repo includes all files and push to GitHub.


# File: requirements.txt
pandas
scikit-learn
matplotlib
seaborn
streamlit
