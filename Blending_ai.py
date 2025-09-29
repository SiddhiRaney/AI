from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

# Load dataset
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Base models
clf1 = LogisticRegression(max_iter=500)
clf2 = RandomForestClassifier(n_estimators=100, random_state=42)
clf3 = GradientBoostingClassifier(n_estimators=100, random_state=42)

# Blending (Voting Classifier)
blend = VotingClassifier(estimators=[
    ('lr', clf1), ('rf', clf2), ('gb', clf3)
], voting='soft')  # 'soft' = uses predicted probabilities

# Train
blend.fit(X_train, y_train)

# Predict & evaluate
y_pred = blend.predict(X_test)
print("Blending Accuracy:", accuracy_score(y_test, y_pred))
