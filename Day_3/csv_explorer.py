# CSV Explorer: Reads and explores the UCI Student Performance dataset using Pandas functions.
import pandas as pd

df = pd.read_csv("student-mat.csv", sep="\t")

print("===== CSV EXPLORER REPORT =====")

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nInfo")
df.info()

print("\nDescribe")
print(df.describe())

print("\nSchool Count")
print(df["school"].value_counts())

print("\nInternet Access Count")
print(df["internet"].value_counts())

print("\nUnique Schools")
print(df["school"].unique())

print("\nNumber of Schools")
print(df["school"].nunique())

print("\nTop 10 Students by G3")
print(df.sort_values("G3", ascending=False).head(10))

print("\nStudents with G3 > 15")
print(df.query("G3 > 15"))

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nMemory Usage")
print(df.memory_usage())

print("\nCorrelation Matrix")
print(df.corr(numeric_only=True))

print("\nTop 5 G3 Scores")
print(df.nlargest(5, "G3"))

print("\nLowest 5 G3 Scores")
print(df.nsmallest(5, "G3"))

print("\n===== REPORT COMPLETED =====")