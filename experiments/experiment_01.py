import sys
import os
import math

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src")
    )
)

from test_problems import (
    problem_1, exact_1,
    problem_2, exact_2,
    problem_3, exact_3
)

from euler import euler
from heun import heun
from rk4 import rk4


step_sizes = [0.1, 0.05, 0.025, 0.0125]

problems = [
    ("Problem 1", problem_1, exact_1),
    ("Problem 2", problem_2, exact_2),
    ("Problem 3", problem_3, exact_3)
]


for problem_name, f, exact in problems:

    print("=" * 50)
    print(problem_name)
    print("=" * 50)

    for h in step_sizes:

        n = int(1 / h)

        x_euler, y_euler = euler(f, 0, 1, h, n)
        x_heun, y_heun = heun(f, 0, 1, h, n)
        x_rk4, y_rk4 = rk4(f, 0, 1, h, n)

        error_euler = abs(exact(1) - y_euler[-1])
        error_heun = abs(exact(1) - y_heun[-1])
        error_rk4 = abs(exact(1) - y_rk4[-1])

        print(f"h = {h}")
        print(f"Euler error = {error_euler}")
        print(f"Heun error = {error_heun}")
        print(f"RK4 error = {error_rk4}")
        print()