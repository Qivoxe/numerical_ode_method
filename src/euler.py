import math
# import numpy as np

def euler(f,x0,y0,h,n):

    x_values = [x0]
    y_values = [y0]

    x = x0
    y = y0

    for i in range(n):
        y = y + h * f(x,y)
        x = x + h

        x_values.append(x)
        y_values.append(y)


    return x_values, y_values



def f(x, y):
    return y


step_sizes = [0.1, 0.05, 0.025, 0.0125]

errors = []

for h in step_sizes:

    n = int(1 / h)

    x, y = euler(f, 0, 1, h, n)

    approximation = y[-1]
    error = abs(math.e - approximation)

    errors.append(error)

    print(f"h = {h}")
    print(f"Euler_approximation = {approximation}")
    print(f"Absolute_error = {error}")
    print()

for i in range(len(errors)-1):
    p = math.log(errors[i]/errors[1+i],2)
    print(f"Order of convergence = {p}")    