"""Plot two linear equations and their intersection."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 6, 300)
fig, ax = plt.subplots()
ax.plot(x, 5 - x, label="x + y = 5")
ax.plot(x, 2 * x - 1, label="2x - y = 1")
ax.scatter([2], [3], color="black", zorder=3, label="solution (2, 3)")
ax.axhline(0, color="0.75", linewidth=0.8)
ax.axvline(0, color="0.75", linewidth=0.8)
ax.set(xlabel="x", ylabel="y", xlim=(-1, 6), ylim=(-1, 7), aspect="equal")
ax.grid(alpha=0.2)
ax.legend()
plt.show()
