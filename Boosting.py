# Boosting example using AdaBoost
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Base estimator
dtree = DecisionTreeClassifier(max_depth=1)

# AdaBoost classifier
boost_clf = AdaBoostClassifier(base_estimator=dtree, n_estimators=50, learning_rate=1.0, random_state=42)

# Train
boost_clf.fit(X_train, y_train)

# Predict
y_pred = boost_clf.predict(X_test)

# Accuracy
print("Boosting Accuracy:", accuracy_score(y_test, y_pred))
