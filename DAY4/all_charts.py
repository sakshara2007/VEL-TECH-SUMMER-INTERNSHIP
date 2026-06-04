import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("student-mat.csv", sep="\t")

# ---------------- BAR CHART ----------------
plt.figure(figsize=(6,4))

school_avg = df.groupby("school")["G3"].mean()

plt.bar(
    school_avg.index,
    school_avg.values
)

plt.title("Average Grade by School")
plt.xlabel("School")
plt.ylabel("Average G3")

plt.show()

# ---------------- SCATTER PLOT ----------------
plt.figure(figsize=(6,4))

plt.scatter(
    df["G1"],
    df["G3"]
)

plt.title("G1 vs G3")
plt.xlabel("G1 Grade")
plt.ylabel("G3 Grade")

plt.show()

# ---------------- HISTOGRAM ----------------
plt.figure(figsize=(6,4))

plt.hist(
    df["age"],
    bins=10
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()

# ---------------- LINE CHART ----------------
plt.figure(figsize=(6,4))

avg_g1 = df["G1"].mean()
avg_g2 = df["G2"].mean()
avg_g3 = df["G3"].mean()

plt.plot(
    ["G1", "G2", "G3"],
    [avg_g1, avg_g2, avg_g3],
    marker="o"
)

plt.title("Average Grade Trend")
plt.xlabel("Exam")
plt.ylabel("Average Grade")

plt.show()
