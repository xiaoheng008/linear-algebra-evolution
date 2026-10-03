"""Vary the input and observe its weighted combination of matrix columns."""

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

A = np.array([[1.0, 2.0], [3.0, 1.0]])
columns = (A[:, 0], A[:, 1])
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.28)
ax.set(xlim=(-5, 7), ylim=(-5, 7), xlabel="first output coordinate", ylabel="second output coordinate", aspect="equal")
ax.axhline(0, color="0.75", linewidth=0.8)
ax.axvline(0, color="0.75", linewidth=0.8)
ax.grid(alpha=0.2)
first = ax.quiver(0, 0, *columns[0], angles="xy", scale_units="xy", scale=1, color="tab:blue")
second = ax.quiver(0, 0, *columns[1], angles="xy", scale_units="xy", scale=1, color="tab:orange")
output = ax.quiver(0, 0, 1, 1, angles="xy", scale_units="xy", scale=1, color="black")
title = ax.set_title("")

ax_x1 = fig.add_axes([0.2, 0.14, 0.65, 0.03])
ax_x2 = fig.add_axes([0.2, 0.08, 0.65, 0.03])
s_x1 = Slider(ax_x1, "x1", -2, 2, valinit=1)
s_x2 = Slider(ax_x2, "x2", -2, 2, valinit=1)

def update(_):
    x = np.array([s_x1.val, s_x2.val])
    y = A @ x
    output.set_UVC(*y)
    output.set_offsets([[0, 0]])
    title.set_text(f"A x = x1 a1 + x2 a2 = ({y[0]:.2f}, {y[1]:.2f})")
    fig.canvas.draw_idle()

s_x1.on_changed(update)
s_x2.on_changed(update)
update(None)
plt.show()
