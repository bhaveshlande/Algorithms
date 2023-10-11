from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# Load the Iris dataset
data = load_iris()
X = data.data
y = (data.target == 2).astype(int)  # Binary classification, detecting Iris-Virginica

# Create and train a logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Make predictions
new_data = np.array([[5.1, 3.5, 1.4, 0.2]])  # Sample feature values for an iris flower
prediction = model.predict(new_data)
if prediction == 1:
    print("Iris-Virginica")
else:
    print("Not Iris-Virginica")
