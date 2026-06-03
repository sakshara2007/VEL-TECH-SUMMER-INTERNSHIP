import pandas as pd

# Group & Compare: Analyzes student performance by study time and gender using grouping and aggregation functions.

df = pd.read_csv("student-mat.csv", sep="\t")

print("===== GROUP & COMPARE REPORT =====")

# 1 Dataset Shape
print("\nDataset Shape")
print(df.shape)

# 2 Average G3 by Study Time
print("\nAverage G3 by Study Time")
print(df.groupby("studytime")["G3"].mean())

# 3 Maximum G3 by Study Time
print("\nMaximum G3 by Study Time")
print(df.groupby("studytime")["G3"].max())

# 4 Minimum G3 by Study Time
print("\nMinimum G3 by Study Time")
print(df.groupby("studytime")["G3"].min())

# 5 Count by Study Time
print("\nStudent Count by Study Time")
print(df.groupby("studytime")["G3"].count())

# 6 Average G3 by Gender
print("\nAverage G3 by Gender")
print(df.groupby("sex")["G3"].mean())

# 7 Maximum G3 by Gender
print("\nMaximum G3 by Gender")
print(df.groupby("sex")["G3"].max())

# 8 Minimum G3 by Gender
print("\nMinimum G3 by Gender")
print(df.groupby("sex")["G3"].min())

# 9 Student Count by Gender
print("\nStudent Count by Gender")
print(df.groupby("sex")["G3"].count())

# 10 Aggregate Statistics
print("\nAggregate Statistics")
print(
    df.groupby("studytime")["G3"]
    .agg(["mean", "max", "min", "count", "sum"])
)

# 11 Top 10 Students
print("\nTop 10 Students by G3")
print(df.nlargest(10, "G3"))

# 12 Bottom 10 Students
print("\nBottom 10 Students by G3")
print(df.nsmallest(10, "G3"))

# 13 School Count
print("\nSchool Count")
print(df["school"].value_counts())

# 14 Internet Access Count
print("\nInternet Access Count")
print(df["internet"].value_counts())

# 15 Study Time Count
print("\nStudy Time Count")
print(df["studytime"].value_counts())

# 16 Reset Index
print("\nMean G3 by Study Time")
print(
    df.groupby("studytime")["G3"]
    .mean()
    .reset_index()
)

# 17 Pivot Table
print("\nPivot Table")
print(
    pd.pivot_table(
        df,
        values="G3",
        index="sex",
        columns="studytime",
        aggfunc="mean"
    )
)

# 18 Correlation with G3
print("\nCorrelation with G3")
print(df.corr(numeric_only=True)["G3"])

# 19 Unique Values
print("\nUnique Values Count")
print(df.nunique())

# 20 Dataset Description
print("\nDataset Description")
print(df.describe())

print("\n===== REPORT COMPLETED =====")