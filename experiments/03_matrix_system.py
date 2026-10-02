"""Change a right-hand side and inspect the solutions of Ax = b."""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2.0, -1.0], [1.0, 3.0]])
b = np.array([1.0, 7.0])
solution = np.linalg.solve(A, b)
print("A =\n", A)
print("b =", b)
print("solution =", solution)
print("check Ax =", A @ solution)

values = np.linspace(-1, 5, 250)
fig, ax = plt.subplots()
ax.plot(values, 2 * values - 1, label="2x - y = 1")
ax.plot(values, (7 - values) / 3, label="x + 3y = 7")
ax.scatter(*solution, color="black", zorder=3, label="solution")
ax.set(xlabel="x", ylabel="y", aspect="equal")
ax.grid(alpha=0.2)
ax.legend()
plt.show()
