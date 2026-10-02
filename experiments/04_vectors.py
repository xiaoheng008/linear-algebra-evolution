"""Observe vector addition and scalar multiplication in the plane."""

import matplotlib.pyplot as plt
import numpy as np

u = np.array([1.0, 2.0])
v = np.array([3.0, -1.0])
vectors = [(u, "u"), (v, "v"), (u + v, "u + v"), (2 * u, "2u")]
fig, ax = plt.subplots()
for vector, label in vectors:
    ax.quiver(0, 0, *vector, angles="xy", scale_units="xy", scale=1, label=label)
ax.set(xlim=(-1, 5), ylim=(-2, 5), xlabel="first coordinate", ylabel="second coordinate", aspect="equal")
ax.axhline(0, color="0.75", linewidth=0.8)
ax.axvline(0, color="0.75", linewidth=0.8)
ax.grid(alpha=0.2)
ax.legend()
plt.show()
