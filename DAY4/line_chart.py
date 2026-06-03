import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student-mat.csv", sep="\t")

plt.plot(
    df["G3"].head(50)
)

plt.title("First 50 Student Grades")
plt.xlabel("Student Number")
plt.ylabel("G3")

plt.show()