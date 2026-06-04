import pandas as pd

# Load Dataset
df = pd.read_csv("student-mat.csv", sep="\t")

# Basic Dataset Information
print("First 5 Records")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns.tolist())

# Top 10 Students by Final Grade
top_students = df.nlargest(10, "G3")

print("\nTop 10 Students")
print(top_students[["age", "studytime", "absences", "G3"]])

# Statistics
print("\nAverage Grade:", df["G3"].mean())
print("Highest Grade:", df["G3"].max())
print("Lowest Grade:", df["G3"].min())

# Sort Top Students
sorted_top = top_students.sort_values(
    by="G3",
    ascending=False
)

print("\nSorted Top Students")
print(sorted_top[["age", "studytime", "G3"]])

# Count Top Students
print("\nNumber of Top Students:", len(top_students))

# Save Result
sorted_top.to_csv(
    "top_students_report.csv",
    index=False
)

print("\nReport Saved Successfully")