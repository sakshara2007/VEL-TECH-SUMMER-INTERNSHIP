import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student-mat.csv", sep="\t")

plt.violinplot(df["G3"])

plt.title("Violin Plot of Final Grades")
plt.ylabel("G3 Grade")

plt.show()
