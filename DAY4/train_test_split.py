import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("student-mat.csv", sep="\t")

X = df[["studytime", "absences", "failures"]]
y = df["G3"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)
print("Training Records:", len(X_train))
print("Testing Records:", len(X_test))