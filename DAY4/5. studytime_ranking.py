import pandas as pd

df = pd.read_csv("student-mat.csv", sep="\t")

ranking = df.groupby(
    "studytime"
)["G3"].mean()

print(ranking)

print(
    "\nBest Study Time Category:"
)

print(
    ranking.idxmax()
)