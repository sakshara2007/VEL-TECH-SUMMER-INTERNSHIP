import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student-mat.csv", sep="\t")

grade_means = [
    df["G1"].mean(),
    df["G2"].mean(),
    df["G3"].mean()
]

plt.fill_between(
    ["G1", "G2", "G3"],
    grade_means
)

plt.title("Average Grade Area Chart")
plt.xlabel("Exams")
plt.ylabel("Average Grade")

plt.show()
