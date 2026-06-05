# Student Grade Prediction

## Project Description
This project predicts student final grades using Machine Learning techniques on the UCI Student Performance Dataset. The project includes data analysis, model training, model comparison, prediction, and data visualization.

## Dataset
- Dataset: UCI Student Performance Dataset
- File: student-mat.csv

## Features Used
- studytime
- absences
- failures

## Models Implemented
1. Linear Regression
2. Ridge Regression

## Model Evaluation
The performance of Linear Regression and Ridge Regression was compared using RMSE (Root Mean Squared Error). The best-performing model was selected and saved as a Pickle (.pkl) file.

## Saved Models
- best_model.pkl
- student_model.pkl

## Prediction Module
The predict.py file loads the saved model and predicts student grades based on input features.

## Data Visualizations
The following charts were created:
1. Area Chart
2. Box Plot
3. Heatmap
4. Horizontal Bar Chart
5. Pie Chart
6. Stem Plot
7. Step Plot
8. Violin Plot

## Files Included
- train_model.py
- predict.py
- ridge_vs_linear.py
- all_additional_charts.py
- student-mat.csv
- best_model.pkl
- student_model.pkl

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## How to Run

Train the model:

```bash
python train_model.py
```

Predict student grades:

```bash
python predict.py
```

Compare Linear Regression and Ridge Regression:

```bash
python ridge_vs_linear.py
```

## Outcome
Successfully built and evaluated Machine Learning models for student grade prediction, saved the best model as a .pkl file, created a prediction module, and developed multiple data visualizations for better data understanding.
