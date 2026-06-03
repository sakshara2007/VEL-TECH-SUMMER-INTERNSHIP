import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Load dataset
df = pd.read_csv("student-mat.csv", sep="\t")

print(df.columns)

# Convert internet column
df["internet"] = df["internet"].map({
    "yes": 1,
    "no": 0
})

# Features
X = df[["studytime", "absences", "failures", "internet"]]

# Target
y = df["G3"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = LinearRegression()

# Training
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# RMSE
rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("RMSE =", rmse)

# New Student Prediction
new_student = [[4, 2, 0, 1]]

result = model.predict(new_student)

print("Predicted Grade =", result[0])