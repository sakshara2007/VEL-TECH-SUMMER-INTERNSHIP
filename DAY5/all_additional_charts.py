import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("student-mat.csv", sep="\t")

# =====================================
# 1. PIE CHART
# =====================================

internet_count = df["internet"].value_counts()

plt.figure(figsize=(6, 4))
plt.pie(
    internet_count,
    labels=internet_count.index,
    autopct="%1.1f%%"
)
plt.title("Internet Usage Distribution")
plt.show()

# =====================================
# 2. BOX PLOT
# =====================================

plt.figure(figsize=(6, 4))
plt.boxplot(df["G3"])
plt.title("Final Grade Distribution")
plt.ylabel("G3 Grade")
plt.show()

# =====================================
# 3. AREA CHART
# =====================================

grade_means = [
    df["G1"].mean(),
    df["G2"].mean(),
    df["G3"].mean()
]

plt.figure(figsize=(6, 4))
plt.fill_between(
    ["G1", "G2", "G3"],
    grade_means
)
plt.title("Average Grade Area Chart")
plt.xlabel("Exams")
plt.ylabel("Average Grade")
plt.show()

# =====================================
# 4. HORIZONTAL BAR CHART
# =====================================

study_avg = df.groupby("studytime")["G3"].mean()

plt.figure(figsize=(6, 4))
plt.barh(
    study_avg.index.astype(str),
    study_avg.values
)
plt.title("Average Grade by Study Time")
plt.xlabel("Average Grade")
plt.ylabel("Study Time")
plt.show()

# =====================================
# 5. HEATMAP
# =====================================

corr = df[
    ["studytime", "absences", "failures", "G1", "G2", "G3"]
].corr()

plt.figure(figsize=(7, 5))
plt.imshow(corr)
plt.colorbar()

plt.xticks(
    range(len(corr.columns)),
    corr.columns,
    rotation=45
)

plt.yticks(
    range(len(corr.columns)),
    corr.columns
)

plt.title("Correlation Heatmap")
plt.show()

# =====================================
# 6. STEM PLOT
# =====================================

sample = df["G3"].head(20)

plt.figure(figsize=(8, 4))
plt.stem(sample)
plt.title("Stem Plot of First 20 Final Grades")
plt.xlabel("Student Number")
plt.ylabel("G3 Grade")
plt.show()

# =====================================
# 7. VIOLIN PLOT
# =====================================

plt.figure(figsize=(6, 4))
plt.violinplot(df["G3"])
plt.title("Violin Plot of Final Grades")
plt.ylabel("G3 Grade")
plt.show()

# =====================================
# 8. STEP PLOT
# =====================================

sample = df["G3"].head(20)

plt.figure(figsize=(8, 4))
plt.step(
    range(len(sample)),
    sample
)

plt.title("Step Plot of First 20 Final Grades")
plt.xlabel("Student Number")
plt.ylabel("G3 Grade")
plt.show()