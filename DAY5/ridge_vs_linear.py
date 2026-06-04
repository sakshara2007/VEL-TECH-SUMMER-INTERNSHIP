import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error
from math import sqrt

# Load Dataset
df = pd.read_csv("student-mat.csv", sep="\t")

# Convert internet column
df["internet"] = df["internet"].map({
    "yes": 1,
    "no": 0
})

# Features
X = df[["studytime", "absences", "failures", "internet"]]

# Target
y = df["G3"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ------------------------
# Linear Regression
# ------------------------

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

linear_pred = linear_model.predict(X_test)

linear_rmse = sqrt(
    mean_squared_error(y_test, linear_pred)
)

# ------------------------
# Ridge Regression
# ------------------------

ridge_model = Ridge(alpha=1.0)

ridge_model.fit(X_train, y_train)

ridge_pred = ridge_model.predict(X_test)

ridge_rmse = sqrt(
    mean_squared_error(y_test, ridge_pred)
)

# ------------------------
# Comparison
# ------------------------

print("Linear RMSE :", round(linear_rmse, 3))
print("Ridge RMSE  :", round(ridge_rmse, 3))

# ------------------------
# Save Best Model
# ------------------------

if linear_rmse < ridge_rmse:
    best_model = linear_model
    model_name = "Linear Regression"
else:
    best_model = ridge_model
    model_name = "Ridge Regression"

with open("best_model.pkl", "wb") as file:
    pickle.dump(best_model, file)

print("\nBest Model:", model_name)
print("best_model.pkl saved successfully!")