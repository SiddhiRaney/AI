# Bagging example using Random Forest
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Base estimator
dtree = DecisionTreeClassifier()

# Bagging classifier
bag_clf = BaggingClassifier(base_estimator=dtree, n_estimators=50, random_state=42)

# Train
bag_clf.fit(X_train, y_train)

# Predict
y_pred = bag_clf.predict(X_test)

# Accuracy
print("Bagging Accuracy:", accuracy_score(y_test, y_pred))
