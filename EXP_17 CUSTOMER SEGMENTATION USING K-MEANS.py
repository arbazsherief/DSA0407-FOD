import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Generate random transaction data
np.random.seed(42)

# Create a dataframe with customer IDs, total amount spent, and frequency of visits
data = pd.DataFrame({
    'CustomerID': range(1, 101),
    'TotalAmount': np.random.normal(100, 20, 100),
    'Frequency': np.random.randint(1, 11, 100)
})

# Display the first few rows of the generated data
print("Generated Transaction Data:")
print(data.head())

# Select relevant features for clustering
X = data[['TotalAmount', 'Frequency']]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters using the Elbow Method
inertia_values = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia_values.append(kmeans.inertia_)

# Plot the Elbow Method to choose the optimal number of clusters
plt.plot(range(1, 11), inertia_values, marker='o')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.show()

# Based on the Elbow Method, choose the optimal number of clusters (K)
optimal_k = 3  # You may need to adjust this based on the plot

# Build the K-Means model with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(X_scaled)

# Add the cluster labels to the original dataset
data['Cluster'] = kmeans.labels_

# Display the number of customers in each cluster
print("\nNumber of customers in each cluster:")
print(data['Cluster'].value_counts())

# Visualize the clusters
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=data['Cluster'], cmap='viridis', alpha=0.5)
plt.title('Customer Segmentation with K-Means')
plt.xlabel('Standardized Total Amount Spent')
plt.ylabel('Standardized Frequency of Visits')
plt.show()
