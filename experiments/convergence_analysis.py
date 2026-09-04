import sys
import os
import math
import matplotlib.pyplot as plt
import numpy as np
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src")
    )
)

from test_problems import problem_1, exact_1
from euler import euler
from heun import heun
from rk4 import rk4


step_sizes = np.array([0.1, 0.05, 0.025, 0.0125])

euler_errors = []
heun_errors = []
rk4_errors = []


for h in step_sizes:

    n = int(1 / h)

    _, y_euler = euler(problem_1, 0, 1, h, n)
    _, y_heun = heun(problem_1, 0, 1, h, n)
    _, y_rk4 = rk4(problem_1, 0, 1, h, n)

    euler_error = abs(exact_1(1) - y_euler[-1])
    heun_error = abs(exact_1(1) - y_heun[-1])
    rk4_error = abs(exact_1(1) - y_rk4[-1])

    euler_errors.append(euler_error)
    heun_errors.append(heun_error)
    rk4_errors.append(rk4_error)


plt.figure(figsize=(8, 6))

plt.loglog(
    step_sizes,
    euler_errors,
    marker="o",
    label="Euler"
)

plt.loglog(
    step_sizes,
    heun_errors,
    marker="s",
    label="Heun"
)

plt.loglog(
    step_sizes,
    rk4_errors,
    marker="^",
    label="RK4"
)

plt.xlabel("Step size h")
plt.ylabel("Absolute error")
plt.title("Convergence of Numerical ODE Methods")

plt.grid(True, which="both")
plt.legend()
# Reference slopes
reference_euler = euler_errors[0] * (step_sizes / step_sizes[0])
reference_heun = heun_errors[0] * (step_sizes / step_sizes[0]) ** 2
reference_rk4 = rk4_errors[0] * (step_sizes / step_sizes[0]) ** 4

plt.loglog(
    step_sizes,
    reference_euler,
    linestyle="--",
    label="O(h)"
)

plt.loglog(
    step_sizes,
    reference_heun,
    linestyle="--",
    label="O(h²)"
)

plt.loglog(
    step_sizes,
    reference_rk4,
    linestyle="--",
    label="O(h⁴)"
)
plt.tight_layout()

results_dir = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../results/figures"
    )
)

os.makedirs(results_dir, exist_ok=True)

output_path = os.path.join(
    results_dir,
    "convergence_comparison.png"
)

plt.savefig(output_path, dpi=300)

print(f"Figure saved to: {output_path}")

plt.show()