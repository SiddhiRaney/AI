from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Base models
clf1 = LogisticRegression(max_iter=500)
clf2 = RandomForestClassifier(n_estimators=100, random_state=42)
clf3 = GradientBoostingClassifier(n_estimators=100, random_state=42)

# Blending (Soft Voting)
blend = VotingClassifier(
    estimators=[('lr', clf1), ('rf', clf2), ('gb', clf3)],
    voting='soft'
)

# Train all models
clf1.fit(X_train, y_train)
clf2.fit(X_train, y_train)
clf3.fit(X_train, y_train)
blend.fit(X_train, y_train)

# Predictions
pred_lr = clf1.predict(X_test)
pred_rf = clf2.predict(X_test)
pred_gb = clf3.predict(X_test)
pred_blend = blend.predict(X_test)

# Accuracies
print("Logistic Regression Accuracy:", accuracy_score(y_test, pred_lr))
print("Random Forest Accuracy:", accuracy_score(y_test, pred_rf))
print("Gradient Boosting Accuracy:", accuracy_score(y_test, pred_gb))
print("Blended Model Accuracy:", accuracy_score(y_test, pred_blend))
print("\n")

# Detailed classification report (Blended Model)
print("Classification Report (Blended Model):")
print(classification_report(y_test, pred_blend))

# Confusion Matrix
cm = confusion_matrix(y_test, pred_blend)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix - Blended Model")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Probability predictions for first 5 samples
probs = blend.predict_proba(X_test[:5])
print("Predicted Probabilities for first 5 test samples:")
print(probs)
