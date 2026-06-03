# Missing Data Detective: Detects, analyzes, and handles missing values in the Student Performance dataset.
import pandas as pd

# Missing Data Detective: Detects, analyzes, and handles missing values in the Student Performance dataset.

df = pd.read_csv("student-mat.csv", sep="\t")

print("===== MISSING DATA DETECTIVE =====")

# 1 Shape
print("\nDataset Shape")
print(df.shape)

# 2 Columns
print("\nColumns")
print(df.columns)

# 3 Missing Values Per Column
print("\nMissing Values Per Column")
print(df.isnull().sum())

# 4 Total Missing Values
print("\nTotal Missing Values")
print(df.isnull().sum().sum())

# 5 Check Any Missing Values
print("\nAny Missing Values?")
print(df.isnull().values.any())

# 6 Count Non-Null Values
print("\nNon-Null Count")
print(df.count())

# 7 Data Types
print("\nData Types")
print(df.dtypes)

# 8 Dataset Info
print("\nInfo")
df.info()

# 9 Numerical Columns
num_cols = df.select_dtypes(include="number").columns
print("\nNumerical Columns")
print(num_cols)

# 10 Categorical Columns
cat_cols = df.select_dtypes(include="object").columns
print("\nCategorical Columns")
print(cat_cols)

# 11 Fill Numeric Nulls with Mean
for col in num_cols:
    df[col] = df[col].fillna(df[col].mean())

# 12 Fill Text Nulls with Unknown
for col in cat_cols:
    df[col] = df[col].fillna("Unknown")

# 13 Verify Missing Values Again
print("\nMissing Values After Filling")
print(df.isnull().sum())

# 14 Dataset Description
print("\nDescription")
print(df.describe())

# 15 First 5 Rows
print("\nHead")
print(df.head())

# 16 Last 5 Rows
print("\nTail")
print(df.tail())

# 17 Duplicate Rows
print("\nDuplicate Rows")
print(df.duplicated().sum())

# 18 Memory Usage
print("\nMemory Usage")
print(df.memory_usage())

# 19 Unique Values Count
print("\nUnique Values")
print(df.nunique())

# 20 Final Shape
print("\nFinal Shape")
print(df.shape)

print("\n===== REPORT COMPLETED =====")