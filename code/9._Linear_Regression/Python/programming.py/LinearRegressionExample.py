from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])

# Create and train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions
new_data = np.array([6]).reshape(-1, 1)
prediction = model.predict(new_data)
print("Linear Regression Prediction:", prediction)
