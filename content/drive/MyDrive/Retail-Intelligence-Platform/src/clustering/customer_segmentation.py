
from sklearn.cluster import KMeans
import pandas as pd

def segment_customers(df):
    features = df[['TotalSpend','Visits','Recency']]

    kmeans = KMeans(n_clusters=4)
    df['Cluster'] = kmeans.fit_predict(features)
    return df, kmeans

if __name__ == "__main__":
    print("Customer segmentation module ready")
