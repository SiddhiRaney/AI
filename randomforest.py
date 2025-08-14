# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load the Iris dataset
data = load_iris()
X = data.data     # Features
y = data.target   # Labels

# Step 2: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Step 3: Initialize Random Forest Classifier
rf_model = RandomForestClassifier(
    n_estimators=100,   # number of trees
    random_state=42
)

# Step 4: Train the model
rf_model.fit(X_train, y_train)

# Step 5: Make predictions
y_pred = rf_model.predict(X_test)

# Step 6: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Step 7: Check feature importance
print("Feature Importances:", rf_model.feature_importances_)
