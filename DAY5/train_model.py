
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load Dataset
df = pd.read_csv("student-mat.csv", sep="\t")

# Features
X = df[["studytime", "absences", "failures"]]

# Target
y = df["G3"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()

model.fit(X_train, y_train)

# Save Model
with open("student_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model Saved Successfully!")