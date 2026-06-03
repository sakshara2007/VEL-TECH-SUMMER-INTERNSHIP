# DataFrame Builder: Creates and analyzes a student DataFrame using various Pandas operations.
import pandas as pd

# Create Student Data
data = {
    "Name": ["Akshara", "Priya", "Ravi", "Kiran", "Divya"],
    "Age": [19, 20, 18, 21, 20],
    "City": ["Chennai", "Madurai", "Salem", "Trichy", "Coimbatore"],
    "Marks": [87, 92, 65, 78, 95]
}

# 1 Create DataFrame
df = pd.DataFrame(data)

# 2 Display DataFrame
print("\nOriginal DataFrame")
print(df)

# 3 Shape
print("\nShape")
print(df.shape)

# 4 Columns
print("\nColumns")
print(df.columns)

# 5 Data Types
print("\nData Types")
print(df.dtypes)

# 6 Head
print("\nHead")
print(df.head())

# 7 Tail
print("\nTail")
print(df.tail())

# 8 Describe
print("\nDescribe")
print(df.describe())

# 9 Add Result Column
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)

# 10 Value Counts
print("\nResult Count")
print(df["Result"].value_counts())

# 11 Sort Values
print("\nSorted by Marks")
print(df.sort_values("Marks", ascending=False))

# 12 Insert Column
df.insert(
    1,
    "Department",
    ["AIDS", "CSE", "IT", "ECE", "AIML"]
)

# 13 LOC
print("\nLOC")
print(df.loc[0:2])

# 14 ILOC
print("\nILOC")
print(df.iloc[0:3])

# 15 Sample
print("\nSample Rows")
print(df.sample(3))

# 16 Rename Column
print("\nRename Column")
print(df.rename(columns={"Marks": "Score"}))

# 17 Set Index
print("\nSet Index")
print(df.set_index("Name"))

# 18 Reset Index
print("\nReset Index")
print(df.reset_index())

# 19 Information
print("\nInfo")
df.info()

# 20 Export CSV
df.to_csv("students.csv", index=False)

print("\nstudents.csv file created successfully")