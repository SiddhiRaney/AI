from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import StackingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Base models
base_models = [
    ('dt', DecisionTreeClassifier(max_depth=3)),
    ('svm', SVC(probability=True, kernel='rbf')),
    ('knn', KNeighborsClassifier(n_neighbors=5)),
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42))
]

# Meta model
meta_model = LogisticRegression(max_iter=1000)

# Stacking model
stack_model = StackingClassifier(estimators=base_models, final_estimator=meta_model, cv=5)

# Train
stack_model.fit(X_train, y_train)

# Predict
y_pred = stack_model.predict(X_test)

# Evaluation
print("🔹 Stacking Accuracy:", accuracy_score(y_test, y_pred))
print("\n🔹 Classification Report:\n", classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, cmap='Blues', fmt='d')
plt.title("Confusion Matrix - Stacking Classifier")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()

# Compare cross-validation scores of base models
print("\n🔹 Base Model Comparison:")
for name, model in base_models:
    scores = cross_val_score(model, X, y, cv=5)
    print(f"{name.upper()} Mean Accuracy: {np.mean(scores):.4f}")

# Stacking model CV performance
stack_scores = cross_val_score(stack_model, X, y, cv=5)
print(f"\n🔹 Stacking Model Mean Accuracy: {np.mean(stack_scores):.4f}")
