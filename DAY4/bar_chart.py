import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student-mat.csv", sep="\t")

avg_grade = df.groupby("studytime")["G3"].mean()

plt.bar(avg_grade.index, avg_grade.values)

plt.title("Average Grade by Study Time")
plt.xlabel("Study Time")
plt.ylabel("Average G3")

plt.show()