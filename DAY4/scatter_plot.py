import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student-mat.csv", sep="\t")

plt.scatter(
    df["absences"],
    df["G3"]
)

plt.title("Absences vs Final Grade")
plt.xlabel("Absences")
plt.ylabel("G3")

plt.show()