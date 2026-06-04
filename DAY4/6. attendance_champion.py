import pandas as pd

df = pd.read_csv("student-mat.csv", sep="\t")

best = df.nsmallest(
    10,
    "absences"
)

print(best[
    ["absences","studytime","G3"]
])

print(
    "\nAverage Grade:"
)

print(best["G3"].mean())