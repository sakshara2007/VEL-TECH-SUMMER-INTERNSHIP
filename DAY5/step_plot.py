import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student-mat.csv", sep="\t")

sample = df["G3"].head(20)

plt.step(
    range(len(sample)),
    sample
)

plt.title("Step Plot of First 20 Final Grades")
plt.xlabel("Student Number")
plt.ylabel("G3 Grade")

plt.show()