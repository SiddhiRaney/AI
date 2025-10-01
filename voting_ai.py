from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define base models
model1 = LogisticRegression(max_iter=1000)
model2 = KNeighborsClassifier(n_neighbors=5)
model3 = DecisionTreeClassifier(random_state=42)

# Create Voting Classifier (Hard Voting)
voting_clf = VotingClassifier(estimators=[
    ('lr', model1),
    ('knn', model2),
    ('dt', model3)
], voting='hard')

# Train
voting_clf.fit(X_train, y_train)

# Predict
y_pred = voting_clf.predict(X_test)

# Evaluate
print("Accuracy (Hard Voting):", accuracy_score(y_test, y_pred))

# ----- Soft Voting (uses predicted probabilities) -----
voting_clf_soft = VotingClassifier(estimators=[
    ('lr', model1),
    ('knn', model2),
    ('dt', model3)
], voting='soft')

voting_clf_soft.fit(X_train, y_train)
y_pred_soft = voting_clf_soft.predict(X_test)
print("Accuracy (Soft Voting):", accuracy_score(y_test, y_pred_soft))
