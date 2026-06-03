import pandas as pd

df = pd.read_csv("student-mat.csv", sep="\t")

x = df["studytime"].tolist()
y = df["G3"].tolist()

n = len(x)

sum_x = sum(x)
sum_y = sum(y)

sum_xy = sum(xi * yi for xi, yi in zip(x, y))
sum_x2 = sum(xi ** 2 for xi in x)

m = (n * sum_xy - sum_x * sum_y) / (
    n * sum_x2 - sum_x ** 2
)

b = (sum_y - m * sum_x) / n

print("Slope:", m)
print("Intercept:", b)

studytime = 4

prediction = m * studytime + b

print("Predicted Grade:", prediction)