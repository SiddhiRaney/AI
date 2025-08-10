import numpy as np

# Calculate a moving average for y2
window_size = 3
moving_avg = np.convolve(y2, np.ones(window_size)/window_size, mode='valid')

# Fill area under y2 for emphasis
plt.fill_between(x, y2, color='green', alpha=0.1)

# Add secondary y-axis for transformed data
fig, ax1 = plt.subplots(figsize=(8, 5))

ax1.plot(x, y, label='Decreasing Line', color='blue', marker='o', linewidth=2)
ax1.plot(x, y2, label='Increasing Line', color='green', linestyle='--', marker='s')
ax1.plot(x, y3, label='Constant Line', color='red', linestyle='-.', marker='^')
ax1.fill_between(x, y2, color='green', alpha=0.1)
ax1.scatter(3, 6, color='purple', s=100, zorder=5, label='Special Point')
ax1.annotate('Peak Value', xy=(1, 10), xytext=(1.5, 11),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

# Secondary axis for moving average
ax2 = ax1.twinx()
ax2.plot(range(2, len(moving_avg)+2), moving_avg, label='Moving Avg (y2)', color='orange', linewidth=2)

# Labels, grid, and legend
ax1.set_xlabel('X Axis')
ax1.set_ylabel('Primary Y Axis')
ax2.set_ylabel('Secondary Y Axis')
ax1.grid(True, linestyle=':', linewidth=0.7)

# Combine legends from both axes
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.title('Enhanced Line Plot with Analysis')
plt.tight_layout()
plt.show()
