"""Compare unique, absent, and non-unique solution sets."""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 4, 300)
cases = [
    ("Unique solution", (2 - x, 4 - 2 * x)),
    ("No solution", (2 - x, 3 - x)),
    ("Infinitely many", (2 - x, 2 - x)),
]
fig, axes = plt.subplots(1, 3, figsize=(12, 3.5))
for ax, (title, (y1, y2)) in zip(axes, cases):
    ax.plot(x, y1, label="first equation")
    ax.plot(x, y2, "--", label="second equation")
    ax.set(title=title, xlabel="x", ylabel="y", xlim=(-1, 4), ylim=(-1, 4))
    ax.grid(alpha=0.2)
axes[0].legend()
fig.tight_layout()
plt.show()
