import matplotlib.pyplot as plt

# ------------------------------------------
# 1️⃣ BASIC LINE PLOT
# ------------------------------------------

# X and Y data
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

plt.figure()  # Create a new figure window
plt.plot(x1, y1)  # Plot x vs y
plt.title("1. Basic Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()


# ------------------------------------------
# 2️⃣ MULTIPLE LINE PLOT
# ------------------------------------------

x2 = [1, 2, 3, 4, 5]
y2_1 = [1, 4, 9, 16, 25]   # square values
y2_2 = [1, 2, 3, 4, 5]     # linear values

plt.figure()
plt.plot(x2, y2_1)  # First line
plt.plot(x2, y2_2)  # Second line
plt.title("2. Multiple Lines")
plt.show()


# ------------------------------------------
# 3️⃣ SCATTER PLOT
# ------------------------------------------

x3 = [5, 7, 8, 7, 2, 17, 9]
y3 = [99, 86, 87, 88, 100, 86, 103]

plt.figure()
plt.scatter(x3, y3)  # Scatter plot
plt.title("3. Scatter Plot")
plt.show()


# ------------------------------------------
# 4️⃣ BAR CHART
# ------------------------------------------

subjects = ["Math", "Physics", "Chemistry", "Biology"]
marks = [85, 90, 78, 92]

plt.figure()
plt.bar(subjects, marks)  # Vertical bars
plt.title("4. Bar Chart")
plt.show()


# ------------------------------------------
# 5️⃣ HORIZONTAL BAR CHART
# ------------------------------------------

plt.figure()
plt.barh(subjects, marks)  # Horizontal bars
plt.title("5. Horizontal Bar Chart")
plt.show()


# ------------------------------------------
# 6️⃣ HISTOGRAM
# ------------------------------------------

marks_hist = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

plt.figure()
plt.hist(marks_hist)  # Histogram groups values into bins
plt.title("6. Histogram")
plt.show()


# ------------------------------------------
# 7️⃣ PIE CHART
# ------------------------------------------

languages = ["Python", "Java", "C++", "JavaScript"]
usage = [40, 25, 20, 15]

plt.figure()
plt.pie(usage, labels=languages, autopct='%1.1f%%')
plt.title("7. Pie Chart")
plt.show()


# ------------------------------------------
# 8️⃣ LINE PLOT WITH GRID
# ------------------------------------------

x8 = [1, 2, 3, 4, 5]
y8 = [10, 20, 25, 30, 40]

plt.figure()
plt.plot(x8, y8)
plt.grid()  # Adds background grid lines
plt.title("8. Plot with Grid")
plt.show()


# ------------------------------------------
# 9️⃣ SUBPLOTS (MULTIPLE GRAPHS IN ONE WINDOW)
# ------------------------------------------

x9 = [1, 2, 3, 4]
y9_1 = [1, 4, 9, 16]
y9_2 = [1, 2, 3, 4]

plt.figure()

# First subplot (1 row, 2 columns, position 1)
plt.subplot(1, 2, 1)
plt.plot(x9, y9_1)
plt.title("Square")

# Second subplot (1 row, 2 columns, position 2)
plt.subplot(1, 2, 2)
plt.plot(x9, y9_2)
plt.title("Linear")

plt.tight_layout()  # Adjust spacing automatically
plt.show()


# ------------------------------------------
# 🔟 SAVE FIGURE
# ------------------------------------------

x10 = [1, 2, 3, 4, 5]
y10 = [5, 4, 3, 2, 1]

plt.figure()
plt.plot(x10, y10)
plt.title("10. Saving Plot")

plt.savefig("my_plot.png")  # Saves plot as image file
plt.show()
