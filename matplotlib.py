import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]

# Additional data for variety
y2 = [2, 4, 6, 8, 10]
y3 = [5, 5, 5, 5, 5]

# Create the plot
plt.figure(figsize=(8, 5))  # Bigger plot
plt.plot(x, y, label='Decreasing Line', color='blue', marker='o', linewidth=2)
plt.plot(x, y2, label='Increasing Line', color='green', linestyle='--', marker='s')
plt.plot(x, y3, label='Constant Line', color='red', linestyle='-.', marker='^')

# Add grid
plt.grid(True, linestyle=':', linewidth=0.7)

# Highlight a specific point
plt.scatter(3, 6, color='purple', s=100, zorder=5, label='Special Point')

# Add annotations
plt.annotate('Peak Value', xy=(1, 10), xytext=(1.5, 11),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

# Labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Enhanced Line Plot')
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
