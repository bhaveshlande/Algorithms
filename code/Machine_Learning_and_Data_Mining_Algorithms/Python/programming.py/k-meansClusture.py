from sklearn.cluster import KMeans
import numpy as np

# Sample data
data = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

# Create and fit a K-Means model
model = KMeans(n_clusters=2)
model.fit(data)

# Get cluster assignments for new data
new_data = np.array([[0, 0], [5, 5]])
predictions = model.predict(new_data)
print("Cluster Assignments:", predictions)
