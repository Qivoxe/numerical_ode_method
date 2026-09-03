import math


def heun(f, x0, y0, h, n):

    x_values = [x0]
    y_values = [y0]

    x = x0
    y = y0

    for i in range(n):

        k1 = f(x, y)

        y_predict = y + h * k1

        k2 = f(x + h, y_predict)

        y = y + (h / 2) * (k1 + k2)

        x = x + h

        x_values.append(x)
        y_values.append(y)

    return x_values, y_values


def f(x, y):
    return y
step_sizes = [0.1, 0.05, 0.025, 0.0125]

errors = []

for h in step_sizes:

    n = int(1/h)

    x, y = heun(f, 0, 1, h, n)

    approximation = y[-1]
    error = abs(math.e - approximation)

    errors.append(error)

    print(f"h = {h}")
    print(f"Heun_approximation = {approximation}")
    print(f"Absolute_error = {error}")
    print()
# print("x =", x)
# print("y =", y)
# print("Heun approximation at x=1:", y[-1])
# print("Exact value:", math.e)
# print("Absolute error:", abs(math.e - y[-1]))
for i in range(len(errors) - 1):
    p = math.log(errors[i] / errors[i + 1], 2)
    print(f"Order of convergence = {p}")