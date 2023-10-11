from sklearn.naive_bayes import GaussianNB
import numpy as np

# Sample data
X = np.array([[1, 2], [2, 3], [2, 1], [3, 3]])
y = np.array([0, 0, 1, 1])

# Create and train a Naive Bayes classifier
model = GaussianNB()
model.fit(X, y)

# Make predictions
new_data = np.array([[1.5, 2.5], [3, 2]])
predictions = model.predict(new_data)
print("Naive Bayes Predictions:", predictions)
