from sklearn.decomposition import PCA
import numpy as np

# Sample data
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Create and fit a PCA model
model = PCA(n_components=2)
model.fit(X)

# Transform the data to lower dimensions
transformed_data = model.transform(X)
print("PCA Transformed Data:", transformed_data)
