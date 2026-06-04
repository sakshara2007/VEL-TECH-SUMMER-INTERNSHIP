import pandas as pd

df = pd.read_csv("student-mat.csv", sep="\t")

print("Dataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nAverage Grade")
print(df["G3"].mean())

print("\nMaximum Grade")
print(df["G3"].max())

print("\nMinimum Grade")
print(df["G3"].min())

print("\nTop 5 Students")
print(
    df.nlargest(
        5,
        "G3"
    )[["G3","studytime"]]
)