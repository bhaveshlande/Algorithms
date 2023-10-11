from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

# Create and train a random forest classifier
model = RandomForestClassifier()
model.fit(X, y)

# Make predictions
new_data = np.array([[5.1, 3.5, 1.4, 0.2]])  # Sample feature values for an iris flower
prediction = model.predict(new_data)
print("Random Forest Prediction:", data.target_names[prediction][0])
