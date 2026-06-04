import pickle
import pandas as pd

# Load Saved Model
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

# New Student Data
new_student = pd.DataFrame({
    "studytime": [3],
    "absences": [2],
    "failures": [0]
})

# Prediction
prediction = model.predict(new_student)

print("Predicted Grade:", round(prediction[0], 2))