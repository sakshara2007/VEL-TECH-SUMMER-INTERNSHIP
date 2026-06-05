import pickle
import pandas as pd

# Load Saved Model
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

# 3 Sample Students
students = pd.DataFrame({
    "studytime": [3, 1, 4],
    "absences": [2, 15, 0],
    "failures": [0, 2, 0]
})

# Predict Grades
predictions = model.predict(students)

# Display Results
for i, pred in enumerate(predictions, start=1):
    print(f"Student {i} Predicted Grade: {round(pred, 2)}")
