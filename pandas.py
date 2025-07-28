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
