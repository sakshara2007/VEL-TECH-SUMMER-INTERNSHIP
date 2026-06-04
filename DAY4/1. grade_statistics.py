import pandas as pd

# Load Dataset
df = pd.read_csv("student-mat.csv", sep="\t")

print("===== GRADE STATISTICS REPORT =====")

print("\nDataset Shape")
print(df.shape)

print("\nFirst 5 Records")
print(df.head())

print("\nAverage Grade")
print(df["G3"].mean())

print("\nHighest Grade")
print(df["G3"].max())

print("\nLowest Grade")
print(df["G3"].min())

print("\nMedian Grade")
print(df["G3"].median())

print("\nStandard Deviation")
print(df["G3"].std())

print("\nGrade Summary")
print(df["G3"].describe())

print("\nTop 5 Grades")
print(df.nlargest(5, "G3")[["studytime","absences","G3"]])