# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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

# Step 7: Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# Step 8: Confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=data.target_names,
            yticklabels=data.target_names)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Step 9: Feature importance visualization
feature_importances = rf_model.feature_importances_
plt.figure(figsize=(8, 5))
plt.bar(range(len(feature_importances)), feature_importances, tick_label=data.feature_names)
plt.title("Feature Importances")
plt.ylabel("Importance Score")
plt.show()

# Step 10: Predict for a new sample
new_sample = np.array([[5.1, 3.5, 1.4, 0.2]])  # Example flower measurements
predicted_class = rf_model.predict(new_sample)
print(f"\nPredicted class for {new_sample}: {data.target_names[predicted_class][0]}")
