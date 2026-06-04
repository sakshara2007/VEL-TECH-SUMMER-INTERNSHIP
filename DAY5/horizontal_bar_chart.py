import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student-mat.csv", sep="\t")

study_avg = df.groupby("studytime")["G3"].mean()

plt.barh(
    study_avg.index.astype(str),
    study_avg.values
)

plt.title("Average Grade by Study Time")
plt.xlabel("Average Grade")
plt.ylabel("Study Time")

plt.show()