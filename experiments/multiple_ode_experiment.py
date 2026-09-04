import sys
import os
import math

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src")
    )
)

from test_problems import problem_2, exact_2
from euler import euler
from heun import heun
from rk4 import rk4


step_sizes = [0.1, 0.05, 0.025, 0.0125]

euler_errors = []
heun_errors = []
rk4_errors = []


for h in step_sizes:

    n = int(1 / h)

    x_euler, y_euler = euler(problem_2, 0, 1, h, n)
    x_heun, y_heun = heun(problem_2, 0, 1, h, n)
    x_rk4, y_rk4 = rk4(problem_2, 0, 1, h, n)

    error_euler = abs(exact_2(1) - y_euler[-1])
    error_heun = abs(exact_2(1) - y_heun[-1])
    error_rk4 = abs(exact_2(1) - y_rk4[-1])

    euler_errors.append(error_euler)
    heun_errors.append(error_heun)
    rk4_errors.append(error_rk4)

    print(f"h = {h}")
    print(f"Euler error = {error_euler}")
    print(f"Heun error = {error_heun}")
    print(f"RK4 error = {error_rk4}")
    print()


print("Euler convergence orders:")

for i in range(len(euler_errors) - 1):
    p = math.log(euler_errors[i] / euler_errors[i + 1], 2)
    print(p)


print("\nHeun convergence orders:")

for i in range(len(heun_errors) - 1):
    p = math.log(heun_errors[i] / heun_errors[i + 1], 2)
    print(p)


print("\nRK4 convergence orders:")

for i in range(len(rk4_errors) - 1):
    p = math.log(rk4_errors[i] / rk4_errors[i + 1], 2)
    print(p)