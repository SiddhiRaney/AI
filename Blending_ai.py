from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Pipelines for models (Logistic Regression benefits from scaling)
clf1 = Pipeline([
    ('scaler', StandardScaler()),
    ('lr', LogisticRegression(max_iter=500))
])

clf2 = RandomForestClassifier(n_estimators=100, random_state=42)
clf3 = GradientBoostingClassifier(n_estimators=100, random_state=42)

# Soft Voting (Blending)
blend = VotingClassifier(
    estimators=[('lr', clf1), ('rf', clf2), ('gb', clf3)],
    voting='soft'
)

# Train only the blended model (it fits all base models)
blend.fit(X_train, y_train)

# Predictions for all models using a loop
models = {
    "Logistic Regression": clf1,
    "Random Forest": clf2,
    "Gradient Boosting": clf3,
    "Blended Model": blend
}

# Fit individual models only after blend (optional)
for m in [clf1, clf2, clf3]:
    m.fit(X_train, y_train)

# Show accuracies
for name, model in models.items():
    pred = model.predict(X_test)
    print(f"{name} Accuracy: {accuracy_score(y_test, pred):.4f}")

print("\nClassification Report (Blended Model):")
pred_blend = blend.predict(X_test)
print(classification_report(y_test, pred_blend))

# Confusion Matrix
cm = confusion_matrix(y_test, pred_blend)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix - Blended Model")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Predicted probabilities (first 5 samples)
print("Predicted Probabilities (first 5 samples):")
print(blend.predict_proba(X_test[:5]))
