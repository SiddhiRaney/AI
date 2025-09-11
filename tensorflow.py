import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import tensorflow as tf

# Save the model
model.save("mnist_model.h5")
print("Model saved as mnist_model.h5")

# Plot training history
history = model.fit(
    x_train, y_train,
    epochs=5,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)

# Plot Accuracy & Loss curves
plt.figure(figsize=(12, 5))

# Accuracy plot
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Acc')
plt.plot(history.history['val_accuracy'], label='Val Acc')
plt.title("Model Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()

# Loss plot
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.title("Model Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()

plt.show()

# Predictions
y_pred = model.predict(x_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)

# Confusion matrix (raw counts)
cm = confusion_matrix(y_true, y_pred_classes)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix (Counts)")
plt.show()

# Normalized confusion matrix (percentages)
cm_norm = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis]
plt.figure(figsize=(8, 6))
sns.heatmap(cm_norm, annot=True, fmt=".2f", cmap="Greens")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix (Normalized)")
plt.show()

# Classification report
print("\nClassification Report:\n")
print(classification_report(y_true, y_pred_classes))

# Per-class accuracy
per_class_acc = cm.diagonal() / cm.sum(axis=1)
plt.figure(figsize=(10, 5))
sns.barplot(x=np.arange(len(per_class_acc)), y=per_class_acc)
plt.xlabel("Class Label")
plt.ylabel("Accuracy")
plt.title("Per-Class Accuracy")
plt.ylim(0, 1)
plt.show()

# Show some predictions
def plot_sample(i):
    plt.imshow(x_test[i], cmap="gray")
    plt.title(f"True: {y_true[i]}, Pred: {y_pred_classes[i]}")
    plt.axis("off")
    plt.show()

print("\nSample Predictions:\n")
for i in range(5):
    plot_sample(i)

# Show misclassified samples
misclassified_idx = np.where(y_true != y_pred_classes)[0]
print(f"\nTotal misclassified samples: {len(misclassified_idx)}")

def plot_misclassified(i):
    plt.imshow(x_test[i], cmap="gray")
    plt.title(f"True: {y_true[i]}, Pred: {y_pred_classes[i]}")
    plt.axis("off")
    plt.show()

print("\nSome Misclassified Samples:\n")
for i in misclassified_idx[:5]:
    plot_misclassified(i)

# Model summary
print("\nModel Summary:\n")
model.summary()

# Count total trainable parameters
trainable_params = np.sum([np.prod(v.shape) for v in model.trainable_variables])
print(f"\nTotal Trainable Parameters: {trainable_params}")
