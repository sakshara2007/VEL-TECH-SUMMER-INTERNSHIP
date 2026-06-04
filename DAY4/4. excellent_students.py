import pandas as pd

df = pd.read_csv("student-mat.csv", sep="\t")

excellent = df[df["G3"] >= 18]

print("Excellent Students")
print(
    excellent[
        ["age","studytime","absences","G3"]
    ]
)

print("\nCount")
print(len(excellent))

print("\nAverage Grade")
print(excellent["G3"].mean())

print("\nMaximum Grade")
print(excellent["G3"].max())