import pandas as pd

# 1. Load sample data (from a dictionary)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 60000, 55000, 70000, 65000]
}

# 2. Create DataFrame
df = pd.DataFrame(data)

# 3. Display the first 3 rows
print("Head of DataFrame:\n", df.head(3))

# 4. Summary statistics
print("\nSummary statistics:\n", df.describe())

# 5. Filter: Employees in the IT department
it_dept = df[df['Department'] == 'IT']
print("\nEmployees in IT:\n", it_dept)

# 6. Add new column: Bonus = 10% of Salary
df['Bonus'] = df['Salary'] * 0.10
print("\nDataFrame with Bonus column:\n", df)

# 7. Group by Department and get average salary
avg_salary = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:\n", avg_salary)

# 8. Sort employees by Salary (descending)
sorted_df = df.sort_values(by='Salary', ascending=False)
print("\nEmployees sorted by Salary:\n", sorted_df)

# 9. Apply a function: Increase salary by 5% for all employees
df['Updated_Salary'] = df['Salary'].apply(lambda x: x * 1.05)
print("\nDataFrame with Updated Salary:\n", df)

# 10. Check for missing values
print("\nMissing values in each column:\n", df.isnull().sum())

# 11. Pivot Table: Average salary per Department
pivot = df.pivot_table(values='Salary', index='Department', aggfunc='mean')
print("\nPivot Table - Average Salary per Department:\n", pivot)

# 12. Merge with another DataFrame (Example: Performance Ratings)
ratings = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Performance': ['Excellent', 'Good', 'Average', 'Excellent', 'Good']
})
merged = pd.merge(df, ratings, on='Name')
print("\nMerged DataFrame with Performance Ratings:\n", merged)

# 13. Save to CSV
df.to_csv("employees.csv", index=False)
print("\nData saved to 'employees.csv'")

# 14. Read from CSV
loaded_df = pd.read_csv("employees.csv")
print("\nData loaded from CSV:\n", loaded_df.head())


# ======================
# iloc Examples
# ======================
print("\n--- iloc Examples ---\n")

# 1. First row
print("1. First row:\n", df.iloc[0], "\n")

# 2. Specific element (row 0, column 1 -> Age of Alice)
print("2. Element at [0,1]:", df.iloc[0, 1], "\n")

# 3. First two rows
print("3. First two rows:\n", df.iloc[0:2], "\n")

# 4. Name & Salary of Alice & Charlie
print("4. Name & Salary of Alice and Charlie:\n", df.iloc[[0, 2], [0, 3]], "\n")

# 5. Entire Age column
print("5. Age column:\n", df.iloc[:, 1], "\n")
