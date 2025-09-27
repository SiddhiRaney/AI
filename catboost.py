from catboost import CatBoostClassifier, Pool
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Example dataset
data = {
    'City': ['Goa', 'Delhi', 'Mumbai', 'Delhi', 'Goa', 'Mumbai'],
    'Age': [23, 45, 34, 25, 52, 43],
    'Purchased': [0, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

X = df[['City', 'Age']]
y = df['Purchased']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Tell CatBoost which columns are categorical
cat_features = ['City']

# Create model
model = CatBoostClassifier(iterations=100, learning_rate=0.1, depth=4, verbose=0)

# Train
model.fit(X_train, y_train, cat_features=cat_features)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
