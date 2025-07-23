import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]

# Create the plot
plt.plot(x, y, label='Sample Line', color='blue', marker='o')

# Add labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Simple Line Plot')
plt.legend()

# Show the plot
plt.show()
