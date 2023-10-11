# Import necessary libraries
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 1: Load and prepare the dataset
data = load_iris()
X = data.data
y = (data.target == 2).astype(int)  # Binary classification, detecting Iris-Virginica

# Step 2: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 3: Create and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 4: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 5: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Step 6: Use the trained model for predictions (e.g., predicting a new data point)
new_data_point = np.array(
    [[5.1, 3.5, 1.4, 0.2]]
)  # Sample feature values for an iris flower
prediction = model.predict(new_data_point)
if prediction == 1:
    print("Iris-Virginica")
else:
    print("Not Iris-Virginica")
