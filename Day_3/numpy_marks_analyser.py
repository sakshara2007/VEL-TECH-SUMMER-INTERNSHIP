# NumPy Marks Analyser: Performs statistical analysis on student marks using NumPy functions.
import numpy as np

marks = np.array([78, 85, 92, 67, 55, 88, 95, 73, 60, 81])

print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Max:", np.max(marks))
print("Min:", np.min(marks))
print("Std:", np.std(marks))
print("Variance:", np.var(marks))
print("Sum:", np.sum(marks))
print("Sorted:", np.sort(marks))
print("Unique:", np.unique(marks))
print("75th Percentile:", np.percentile(marks, 75))
print("Argmax:", np.argmax(marks))
print("Argmin:", np.argmin(marks))
print("Pass/Fail:", np.where(marks >= 50, "Pass", "Fail"))
print("Passed Count:", np.count_nonzero(marks >= 50))

reshaped = marks.reshape(2,5)
print("Reshape:\n", reshaped)
print("Transpose:\n", reshaped.T)

print("Cumsum:", np.cumsum(marks))
print("Cumprod:", np.cumprod(marks))
print("Average:", np.average(marks))
print("Range:", np.ptp(marks))