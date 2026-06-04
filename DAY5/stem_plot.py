import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student-mat.csv", sep="\t")

sample = df["G3"].head(20)

plt.stem(sample)

plt.title("Stem Plot of First 20 Final Grades")
plt.xlabel("Student Number")
plt.ylabel("G3 Grade")

plt.show()