import math

def rk4(f,x0,y0,h,n):

    x_values = [x0]
    y_values = [y0]

    x = x0
    y = y0

    for i in range(n):
               
        k1 = f(x, y)

        k2 = f(x + h / 2, y + h * k1 / 2)

        k3 = f(x + h / 2, y + h * k2 / 2)

        k4 = f(x + h, y + h * k3)

        y = y + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)

        x = x + h

        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

def f(x,y):
    return y
step_sizes = [0.1, 0.05, 0.025, 0.0125]
errors = []
for h in step_sizes:

    n = int(1/h)

    x,y = rk4(f,0,1,h, n)


    approximation = y[-1]
    error = abs(math.e - approximation)


    errors.append(error)


for i in range (len(errors)-1):
    p = math.log(errors[i]/errors[i+1],2)
    print(f"Order of convergence = {p}")