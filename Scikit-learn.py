# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# 1️⃣ Load dataset
iris = load_iris()
X = iris.data      # Features
y = iris.target    # Labels

# 2️⃣ Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3️⃣ Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4️⃣ Train a Support Vector Machine (SVM) classifier
clf = SVC(kernel='linear', C=1.0, random_state=42)
clf.fit(X_train, y_train)

# 5️⃣ Make predictions
y_pred = clf.predict(X_test)

# 6️⃣ Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

from sklearn.model_selection import GridSearchCV

param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf', 'poly'],
    'gamma': ['scale', 'auto']
}

grid = GridSearchCV(SVC(), param_grid, cv=5, scoring='accuracy')
grid.fit(X_train, y_train)

print("Best Parameters:", grid.best_params_)
y_pred = grid.predict(X_test)
print("Accuracy after tuning:", accuracy_score(y_test, y_pred))

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# ----------------------------------------------------------
# 7️⃣ Plot Confusion Matrix (Visualization)
# ----------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.title("Confusion Matrix Heatmap")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


# ----------------------------------------------------------
# 8️⃣ PCA Visualization (2D plot of SVM decision boundaries)
# ----------------------------------------------------------
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

clf_pca = SVC(kernel='rbf', C=1)
clf_pca.fit(X_train_pca, y_train)

plt.figure(figsize=(6,5))

# scatter actual data points
plt.scatter(X_train_pca[:,0], X_train_pca[:,1], c=y_train, cmap="viridis")
plt.title("PCA Visualization of Iris Dataset")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.colorbar(label="Classes")
plt.show()


# ----------------------------------------------------------
# 9️⃣ ROC Curve (One-vs-Rest for Multi-Class SVM)
# ----------------------------------------------------------
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc
from sklearn.multiclass import OneVsRestClassifier

# Binarize labels for multi-class ROC
y_bin = label_binarize(y_train, classes=[0, 1, 2])
n_classes = y_bin.shape[1]

# Train OVR classifier
ovr_clf = OneVsRestClassifier(SVC(kernel='rbf', probability=True))
ovr_clf.fit(X_train, y_bin)
y_score = ovr_clf.predict_proba(X_test)

# Plot ROC curves
plt.figure(figsize=(7,5))
for i in range(n_classes):
    fpr, tpr, _ = roc_curve(label_binarize(y_test, classes=[0,1,2])[:, i], y_score[:, i])
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=f"Class {i} (AUC = {roc_auc:.2f})")

plt.plot([0,1], [0,1], 'k--')
plt.title("Multi-class ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()


# ----------------------------------------------------------
# 🔟 Save & Load the Model
# ----------------------------------------------------------
import joblib

# Save the best model
joblib.dump(grid.best_estimator_, "best_svm_model.joblib")
print("Model saved as: best_svm_model.joblib")

# Load it again
loaded_model = joblib.load("best_svm_model.joblib")
print("Loaded model accuracy:", loaded_model.score(X_test, y_test))

