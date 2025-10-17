# 📦 Install Required Libraries (Run this in terminal / notebook)
# pip install pandas pyjanitor missingno numpy

import pandas as pd
import numpy as np
import janitor  # from pyjanitor
import missingno as msno

# 🧹 Load Your Dataset
df = pd.read_csv("your_file.csv")  # or .xlsx, .json etc.

# 🔠 1. Clean Column Names (lowercase, replace spaces with _)
df = df.clean_names()

# 🔍 2. Drop Completely Empty Columns or Rows
df = df.dropna(axis=1, how='all')  # Remove empty columns
df = df.dropna(axis=0, how='all')  # Remove empty rows

# 📌 3. Remove Duplicates
df = df.drop_duplicates()

# 🔄 4. Fill Missing Values (Numeric / Categorical)
df = df.fill_missing(value=0)  # fill numeric NaNs with 0
df = df.fill_missing(value="Unknown", columns=['name', 'category'])  # for categorical

# 🔢 5. Convert Data Types Automatically
df = df.convert_dtypes()

# 📏 6. Remove Outliers (Example for 'price' column using IQR)
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
df = df[~((df['price'] < (Q1 - 1.5 * IQR)) | (df['price'] > (Q3 + 1.5 * IQR)))]

# 📊 7. Visualize Missing Data (Optional)
msno.matrix(df)  # or msno.bar(df)

# ✅ Final Cleaned Data
print(df.head())
df.to_csv("cleaned_output.csv", index=False)
