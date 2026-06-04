import pandas as pd

df = pd.read_csv("student-mat.csv", sep="\t")

weak_students = df[df["G3"] < 8]

print("Weak Students")
print(
    weak_students[
        ["age","studytime","failures","G3"]
    ]
)

print("\nTotal Weak Students")
print(len(weak_students))

print("\nAverage Grade")
print(
    weak_students["G3"].mean()
)

print("\nHighest Grade")
print(
    weak_students["G3"].max()
)

print("\nLowest Grade")
print(
    weak_students["G3"].min()
)