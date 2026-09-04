import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import matplotlib.pyplot as plt
import math
import numpy as np
from euler import euler
from heun import heun

def f(x,y):
    return y


h = 0.1
n = int(1/h)

x_euler, y_euler = euler(f,0,1,h,n)
x_heun, y_heun = heun(f,0,1,h,n)

x_exact = np.linspace(0, 1, 100)
y_exact = np.exp(x_exact)

plt.plot(x_exact,y_exact, label = "Exact Solution")
plt.plot(x_euler,y_euler, marker="o", label = "Euler")
plt.plot(x_heun,y_heun, marker="o", label = "Heun")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Euler vs Heun vs Exact Solution")
plt.legend()
plt.grid(True)

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

figure_path = os.path.join(
    project_root,
    "results",
    "figures",
    "euler_vs_heun.png"
)

plt.savefig(figure_path, dpi=300)
plt.show