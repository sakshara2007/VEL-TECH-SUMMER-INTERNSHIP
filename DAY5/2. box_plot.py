import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student-mat.csv", sep="\t")

plt.boxplot(df["G3"])

plt.title("Final Grade Distribution")
plt.ylabel("G3 Grade")

plt.show()
