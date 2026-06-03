import pandas as pd

# Full EDA Report: Performs comprehensive exploratory data analysis on the Student Performance dataset.

df = pd.read_csv("student-mat.csv", sep="\t")

print("===== FULL EDA REPORT =====")

# 1 Shape
print("\nDataset Shape")
print(df.shape)

# 2 Columns
print("\nColumn Names")
print(df.columns)

# 3 Data Types
print("\nData Types")
print(df.dtypes)

# 4 Head
print("\nFirst 5 Rows")
print(df.head())

# 5 Tail
print("\nLast 5 Rows")
print(df.tail())

# 6 Sample Rows
print("\nRandom Sample")
print(df.sample(5))

# 7 Dataset Info
print("\nDataset Info")
df.info()

# 8 Statistical Summary
print("\nStatistical Summary")
print(df.describe())

# 9 Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# 10 Total Missing Values
print("\nTotal Missing Values")
print(df.isnull().sum().sum())

# 11 Duplicate Rows
print("\nDuplicate Rows")
print(df.duplicated().sum())

# 12 Unique Values
print("\nUnique Values Count")
print(df.nunique())

# 13 Memory Usage
print("\nMemory Usage")
print(df.memory_usage())

# 14 Numerical Columns
print("\nNumerical Columns")
print(df.select_dtypes(include="number").columns)

# 15 Categorical Columns
print("\nCategorical Columns")
print(df.select_dtypes(include="object").columns)

# 16 Correlation Matrix
print("\nCorrelation Matrix")
print(df.corr(numeric_only=True))

# 17 Mean Values
print("\nMean Values")
print(df.mean(numeric_only=True))

# 18 Median Values
print("\nMedian Values")
print(df.median(numeric_only=True))

# 19 Standard Deviation
print("\nStandard Deviation")
print(df.std(numeric_only=True))

# 20 Top 10 Students by G3
print("\nTop 10 Students by G3")
print(df.nlargest(10, "G3"))

# 21 Bottom 10 Students by G3
print("\nBottom 10 Students by G3")
print(df.nsmallest(10, "G3"))

# 22 School Distribution
print("\nSchool Distribution")
print(df["school"].value_counts())

# 23 Gender Distribution
print("\nGender Distribution")
print(df["sex"].value_counts())

# 24 Internet Access Distribution
print("\nInternet Access Distribution")
print(df["internet"].value_counts())

# 25 Study Time Distribution
print("\nStudy Time Distribution")
print(df["studytime"].value_counts())

print("\n===== EDA REPORT COMPLETED =====")