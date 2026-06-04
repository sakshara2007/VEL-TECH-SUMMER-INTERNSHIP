import pandas as pd

df = pd.read_csv("student-mat.csv", sep="\t")

report = df.groupby(
    "failures"
)["G3"].mean()

print(report)

print(
    "\nBest Failure Group:"
)

print(report.idxmax())
