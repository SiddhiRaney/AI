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


# 6. Last row
print("6. Last row:\n", df.iloc[-1], "\n")

# 7. Last 3 rows
print("7. Last 3 rows:\n", df.iloc[-3:], "\n")

# 8. Rows 1 to 3 and columns 'Name' & 'Age'
print("8. Rows 1 to 3 with Name & Age:\n", df.iloc[1:4, [0, 1]], "\n")

# 9. Salary column using iloc (alternative way)
print("9. Salary column:\n", df.iloc[:, df.columns.get_loc('Salary')], "\n")

# 10. Every alternate row (step slicing)
print("10. Every alternate row:\n", df.iloc[::2], "\n")
# ======================
# loc Examples
# ======================
print("\n--- loc Examples ---\n")

# 15. Select row by label
print("15. Row with index 0:\n", df.loc[0], "\n")

# 16. Select specific columns
print("16. Name & Salary columns:\n", df.loc[:, ['Name', 'Salary']], "\n")

# 17. Filter using loc (Age > 25)
print("17. Employees with Age > 25:\n", df.loc[df['Age'] > 25], "\n")

# 18. Select rows and columns together
print("18. Name & Department of first 3 employees:\n",
      df.loc[0:2, ['Name', 'Department']], "\n")


# ======================
# Conditional Filtering
# ======================
print("\n--- Conditional Filtering ---\n")

# 19. Multiple conditions
high_paid_it = df[(df['Department'] == 'IT') & (df['Salary'] > 65000)]
print("19. IT employees with Salary > 65000:\n", high_paid_it, "\n")

# 20. isin()
print("20. Employees from HR or Finance:\n",
      df[df['Department'].isin(['HR', 'Finance'])], "\n")


# ======================
# Value Counts & Unique
# ======================
print("\n--- Value Counts & Unique ---\n")

# 21. Count employees per department
print("21. Department counts:\n", df['Department'].value_counts(), "\n")

# 22. Unique departments
print("22. Unique departments:\n", df['Department'].unique(), "\n")


# ======================
# Renaming & Dropping
# ======================
print("\n--- Renaming & Dropping ---\n")

# 23. Rename column
df_renamed = df.rename(columns={'Updated_Salary': 'Final_Salary'})
print("23. Renamed column:\n", df_renamed.head(), "\n")

# 24. Drop column
df_dropped = df.drop(columns=['Bonus'])
print("24. After dropping Bonus column:\n", df_dropped.head(), "\n")


# ======================
# Sorting & Ranking
# ======================
print("\n--- Sorting & Ranking ---\n")

# 25. Sort by Age
print("25. Sorted by Age:\n", df.sort_values('Age'), "\n")

# 26. Rank employees by Salary
df['Salary_Rank'] = df['Salary'].rank(ascending=False)
print("26. Salary Rank:\n", df[['Name', 'Salary', 'Salary_Rank']], "\n")


# ======================
# String Operations
# ======================
print("\n--- String Operations ---\n")

# 27. Convert names to uppercase
df['Name_Upper'] = df['Name'].str.upper()
print("27. Uppercase Names:\n", df[['Name', 'Name_Upper']], "\n")

# 28. Check names starting with 'A'
print("28. Names starting with A:\n",
      df[df['Name'].str.startswith('A')], "\n")


# ======================
# Handling Missing Data (Demo)
# ======================
print("\n--- Missing Data Handling ---\n")

# 29. Introduce missing value
df.loc[2, 'Salary'] = None

# 30. Fill missing values
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print("30. After filling missing Salary:\n", df, "\n")


# ======================
# Apply & Map
# ======================
print("\n--- Apply & Map ---\n")

# 31. Apply function to column
df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Senior')
print("31. Age Groups:\n", df[['Name', 'Age', 'Age_Group']], "\n")

# 32. Map department codes
dept_map = {'HR': 'Human Resources', 'IT': 'Information Tech', 'Finance': 'Finance'}
df['Dept_Full'] = df['Department'].map(dept_map)
print("32. Mapped Department Names:\n", df[['Department', 'Dept_Full']], "\n")
