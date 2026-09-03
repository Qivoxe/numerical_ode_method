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

x, y = euler(f, 0, 1, 0.1, 10) 
print("x =", x) 
print("y =", y) 
print("Euler approximation at x=1:", y[-1]) 
print("Exact value:", math.e) 
print("Absolute error:", abs(math.e - y[-1]))    

