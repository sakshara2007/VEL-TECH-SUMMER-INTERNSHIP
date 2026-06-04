import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("student-mat.csv", sep="\t")

# Internet Usage Count
internet_count = df["internet"].value_counts()

plt.pie(
    internet_count,
    labels=internet_count.index,
    autopct="%1.1f%%"
)

plt.title("Internet Usage Distribution")

plt.show()