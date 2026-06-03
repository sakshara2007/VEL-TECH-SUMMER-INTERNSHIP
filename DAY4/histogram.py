import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student-mat.csv", sep="\t")

plt.hist(
    df["G3"],
    bins=10
)

plt.title("Distribution of Final Grades")
plt.xlabel("G3")
plt.ylabel("Students")

plt.show()