"""重新生成正文中的静态配图（中文标注）。

用法：python3 scripts/make_figures.py [图名 ...]
不带参数时生成全部图片，输出到 content/book/chNN/ 下。
需要 matplotlib、numpy，以及一款能显示简体中文的字体。
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[1] / "content" / "book"

CJK_FONTS = ["Hiragino Sans GB", "PingFang SC", "Noto Sans CJK SC",
             "Source Han Sans SC", "Microsoft YaHei", "Heiti TC"]
available = {f.name for f in font_manager.fontManager.ttflist}
font = next((name for name in CJK_FONTS if name in available), None)
if font is None:
    sys.exit("找不到中文字体，请安装 Noto Sans CJK SC 等字体后重试。")

plt.rcParams.update({
    "font.family": [font, "DejaVu Sans"],
    "mathtext.fontset": "dejavusans",
    "axes.unicode_minus": True,
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": "#8a8984",
    "axes.labelcolor": "#2b2b29",
    "xtick.color": "#52514e",
    "ytick.color": "#52514e",
    "text.color": "#0b0b0b",
    "legend.frameon": False,
    "figure.dpi": 160,
    "savefig.dpi": 160,
    "savefig.bbox": "tight",
    "savefig.facecolor": "white",
})

# 分类色固定顺序：蓝、橙、青绿、红、紫；灰色用于辅助元素。
BLUE, ORANGE, AQUA, RED, VIOLET = "#2a78d6", "#eb6834", "#1baf7a", "#e34948", "#4a3aa7"
GRAY, LIGHT = "#52514e", "#c9c8c2"


def arrow(ax, start, end, color, lw=2.6, ls="-", zorder=3):
    ax.annotate("", xy=end, xytext=start, zorder=zorder,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, ls=ls,
                                shrinkA=0, shrinkB=0, mutation_scale=16))


def axes_cross(ax):
    ax.axhline(0, color=LIGHT, lw=0.9, zorder=0)
    ax.axvline(0, color=LIGHT, lw=0.9, zorder=0)
    ax.grid(alpha=0.25)


def save(fig, chapter, name):
    path = ROOT / chapter / name
    fig.savefig(path)
    plt.close(fig)
    print("wrote", path.relative_to(ROOT.parents[1]))


def grid_lines(ax, matrix, lim=2, colors=(BLUE, ORANGE), alpha=0.35):
    """画出输入网格 [-lim, lim]^2 在 matrix 作用后的样子。"""
    ts = np.linspace(-lim, lim, 2)
    for k in range(-lim, lim + 1):
        horizontal = matrix @ np.vstack([ts, np.full(2, k)])
        vertical = matrix @ np.vstack([np.full(2, k), ts])
        ax.plot(*horizontal, color=colors[0], lw=1, alpha=alpha)
        ax.plot(*vertical, color=colors[1], lw=1, alpha=alpha)


def unit_square(ax, matrix, color=AQUA):
    square = matrix @ np.array([[0, 1, 1, 0], [0, 0, 1, 1]])
    ax.fill(*square, color=color, alpha=0.22, lw=0)


# ---------------------------------------------------------------- 第 1 章
def ch01_recipe():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10, 4.1),
                                 gridspec_kw={"width_ratios": [1.15, 1]})
    x = np.linspace(0, 5.2, 50)
    ax.plot(x, (50 - 10 * x) / 20, color=BLUE, lw=2.2, label="蛋白质 50 克：$10x+20y=50$")
    ax.plot(x, (40 - 20 * x) / 10, color=ORANGE, lw=2.2, label="脂肪 40 克：$20x+10y=40$")
    ax.scatter([1], [2], s=90, color=AQUA, zorder=4, edgecolor="white", lw=1.5)
    ax.annotate("(1, 2)  两项都满足", (1, 2), xytext=(10, 8), textcoords="offset points",
                color="#0b0b0b")
    ax.scatter([3], [1], s=70, color=RED, zorder=4, edgecolor="white", lw=1.5)
    ax.annotate("(3, 1)  只满足蛋白质", (3, 1), xytext=(6, 10), textcoords="offset points",
                color="#0b0b0b")
    ax.set(xlim=(-0.2, 5.3), ylim=(-0.2, 4.2), xlabel="甲的份数 $x$（每份 100 克）",
           ylabel="乙的份数 $y$（每份 100 克）", title="每项要求是一条线，交点同时满足")
    axes_cross(ax)
    ax.legend(loc="upper right", fontsize=10)

    pos = np.arange(2)
    bx.bar(pos - 0.19, [50, 70], width=0.36, color=[BLUE, ORANGE], label="配方 (3, 1) 实际含量")
    bx.bar(pos + 0.19, [50, 40], width=0.36, facecolor="white", edgecolor=GRAY, lw=1.6,
           hatch="//", label="目标")
    for p, v in zip(pos - 0.19, [50, 70]):
        bx.text(p, v + 2, f"{v}", ha="center", color="#0b0b0b")
    for p, v in zip(pos + 0.19, [50, 40]):
        bx.text(p, v + 2, f"{v}", ha="center", color=GRAY)
    bx.set(xticks=pos, xticklabels=["蛋白质", "脂肪"], ylabel="克", ylim=(0, 90),
           title="把 (3, 1) 读回成分：错在脂肪")
    bx.grid(axis="y", alpha=0.25)
    bx.legend(loc="upper left", fontsize=10)
    fig.tight_layout()
    save(fig, "ch01", "recipe-constraints.png")


# ---------------------------------------------------------------- 第 3 章
def ch03_house():
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    a = np.linspace(1.5, 2.5, 50)
    ax.plot(a, 150 - 80 * a, color=BLUE, lw=2.2, label="甲房：$80\\alpha+\\beta=150$")
    ax.plot(a, (180 - 100 * a) / 2, color=ORANGE, lw=2.2, label="乙房：$100\\alpha+2\\beta=180$")
    ax.scatter([2], [-10], s=90, color=AQUA, zorder=4, edgecolor="white", lw=1.5)
    ax.annotate("(2, −10)  两套房都算对", (2, -10), xytext=(12, 4), textcoords="offset points")
    ax.set(xlim=(1.5, 2.5), ylim=(-50, 30), xlabel="面积系数 $\\alpha$（万元/平方米）",
           ylabel="距离系数 $\\beta$（万元/公里）", title="每套房约束同一组系数")
    ax.grid(alpha=0.25)
    ax.legend(loc="upper right", fontsize=10)
    fig.tight_layout()
    save(fig, "ch03", "house-price-constraints.png")


# ---------------------------------------------------------------- 第 4 章
def ch04_displacement():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10, 4.4))
    arrow(ax, (0, 0), (1, 2), BLUE)
    arrow(ax, (1, 2), (4, 1), ORANGE)
    arrow(ax, (0, 0), (4, 1), AQUA, lw=2.2, ls="--")
    ax.text(0.62, 0.95, "第一段 (1, 2)", color="#0b0b0b")
    ax.text(2.6, 1.75, "第二段 (3, −1)", color="#0b0b0b")
    ax.text(2.3, 0.2, "总位移 (4, 1)", color="#0b0b0b")
    ax.set(xlim=(-0.6, 4.6), ylim=(-0.6, 2.8), aspect="equal", xlabel="向右（米）",
           ylabel="向上（米）", title="相加：首尾相接")
    axes_cross(ax)

    bx.plot([-2, 3], [-4, 6], color=LIGHT, lw=1, ls=":", zorder=0)
    arrow(bx, (0, 0), (2, 4), AQUA, lw=2.2)
    arrow(bx, (0, 0), (1, 2), BLUE, lw=3.2)
    arrow(bx, (0, 0), (-1, -2), RED, lw=2.4)
    bx.text(2.25, 3.0, "2·(1, 2) = (2, 4)\n拉长一倍", color="#0b0b0b")
    bx.text(1.15, 1.5, "(1, 2)", color="#0b0b0b")
    bx.text(-0.85, -2.3, "−1·(1, 2) = (−1, −2)\n方向掉头", color="#0b0b0b", va="top")
    bx.set(xlim=(-2.6, 5.2), ylim=(-3.6, 4.6), aspect="equal", xlabel="向右（米）",
           ylabel="向上（米）", title="数乘：拉长、缩短或掉头")
    axes_cross(bx)
    fig.tight_layout()
    save(fig, "ch04", "displacement.png")


def ch04_rope():
    fig, ax = plt.subplots(figsize=(4.8, 5.6))
    ax.plot([-30, 30], [40, 40], color=LIGHT, ls="--", lw=1)
    arrow(ax, (0, 0), (-30, 40), BLUE)
    arrow(ax, (0, 0), (30, 40), ORANGE)
    arrow(ax, (0, 0), (0, -80), RED)
    ax.scatter([0], [0], color="#0b0b0b", s=24, zorder=5)
    ax.text(-31, 45, "左绳 (−30, 40)", ha="center")
    ax.text(31, 45, "右绳 (30, 40)", ha="center")
    ax.text(4, -72, "重力 (0, −80)")
    ax.set(xlim=(-62, 62), ylim=(-92, 62), aspect="equal", xlabel="水平分量（牛顿）",
           ylabel="竖直分量（牛顿）", title="两绳拉力加重力，总和为零")
    axes_cross(ax)
    fig.tight_layout()
    save(fig, "ch04", "rope-balance.png")


# ---------------------------------------------------------------- 第 5 章
def ch05_forces():
    u, v = np.array([-0.6, 0.8]), np.array([0.6, 0.8])
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 5), sharey=True)
    for ax, (tl, tr), title in zip(axes, [(50, 50), (25, 75)],
                                   ["左 50、右 50：合力竖直向上", "左 25、右 75：合力偏向右边"]):
        left, right = tl * u, tr * v
        total = left + right
        arrow(ax, (0, 0), left, BLUE)
        arrow(ax, left, total, ORANGE)
        arrow(ax, (0, 0), total, AQUA, lw=2.2, ls="--")
        ax.text(*(left / 2 + np.array([-3, 0])), f"左绳 {tl} 牛顿", ha="right", va="center")
        ax.text(*((left + total) / 2 + np.array([-4, 4])), f"右绳 {tr} 牛顿", ha="right",
                va="center")
        ax.text(total[0] + 2, total[1] + 3, f"合力 ({total[0]:.0f}, {total[1]:.0f})",
                ha="center")
        ax.set(xlim=(-55, 60), ylim=(-8, 95), aspect="equal", xlabel="水平分量（牛顿）",
               title=title)
        axes_cross(ax)
    axes[0].set_ylabel("竖直分量（牛顿）")
    fig.tight_layout()
    save(fig, "ch05", "force-combination.png")


# ---------------------------------------------------------------- 第 8 章
def ch08_stereo():
    t = np.linspace(0, 1, 800)
    M = 0.4 * np.sin(2 * np.pi * 3 * t)
    S = 0.2 * np.sin(2 * np.pi * 7 * t)
    L, R = M + S, M - S
    fig, axes = plt.subplots(3, 1, figsize=(9, 6.4), sharex=True, sharey=True)
    rows = [
        (L, R, "左声道 L", "右声道 R", "原来的记录：左、右声道"),
        (M, S, "共同部分 M", "差别部分 S", "同一信号换一种完整记录：共同与差别"),
        (L, M, "原左声道 L", "只留 M 时还原的左声道", "丢掉差别 S，左声道无法还原"),
    ]
    for ax, (a, b, la, lb, title) in zip(axes, rows):
        ax.plot(t, a, color=BLUE, lw=1.8, label=la)
        ax.plot(t, b, color=ORANGE, lw=1.8, ls="--", label=lb)
        ax.set_title(title, loc="left")
        ax.set_ylabel("采样值")
        ax.grid(alpha=0.25)
        ax.legend(loc="upper right", ncol=2, fontsize=10)
    axes[-1].set_xlabel("时间（秒）")
    axes[0].set_ylim(-0.75, 0.85)
    fig.tight_layout()
    save(fig, "ch08", "stereo-basis.png")


# ---------------------------------------------------------------- 第 9 章
def ch09_plane():
    from itertools import product
    u, v = np.array([1., 0., 1.]), np.array([0., 1., 1.])
    coeffs = np.array(list(product(np.linspace(-1.5, 1.5, 9), repeat=2)))
    samples = coeffs @ np.stack([u, v])
    target = np.array([1.5, 0.5, 2.0])
    fig = plt.figure(figsize=(10.5, 5))
    ax = fig.add_subplot(1, 2, 1)
    bx = fig.add_subplot(1, 2, 2, projection="3d")
    ax.scatter(samples[:, 0], samples[:, 1], s=16, color=AQUA, alpha=0.45, label="部分组合 $su+tv$")
    arrow(ax, (0, 0), u[:2], BLUE)
    arrow(ax, (0, 0), v[:2], ORANGE)
    box = dict(facecolor="white", edgecolor="none", pad=1.5)
    ax.text(1.0, -0.28, "u 的前两项 (1, 0)", color="#0b0b0b", bbox=box)
    ax.text(-0.1, 1.08, "v 的前两项 (0, 1)", color="#0b0b0b", ha="right", bbox=box)
    ax.scatter(*target[:2], marker="*", s=180, color=RED, zorder=5, label="目标的前两项 (1.5, 0.5)")
    ax.set(xlim=(-2.4, 2.4), ylim=(-2.4, 2.4), aspect="equal", xlabel="第一坐标 $x=s$",
           ylabel="第二坐标 $y=t$", title="只看前两个坐标")
    axes_cross(ax)
    ax.legend(loc="lower left", fontsize=9.5)

    gs, gt = np.meshgrid(np.linspace(-2, 2, 5), np.linspace(-2, 2, 5))
    bx.plot_wireframe(gs, gt, gs + gt, color="#aab6be", alpha=0.35, lw=0.7)
    bx.scatter(*samples.T, s=10, alpha=0.4, color=AQUA)
    bx.quiver(0, 0, 0, *u, color=BLUE, lw=3, arrow_length_ratio=0.15)
    bx.quiver(0, 0, 0, *v, color=ORANGE, lw=3, arrow_length_ratio=0.15)
    bx.text(*(1.2 * u), "u", color="#0b0b0b", fontsize=13)
    bx.text(*(1.2 * v), "v", color="#0b0b0b", fontsize=13)
    bx.scatter(*target, marker="*", s=160, color=RED)
    bx.text(*(target + [0.2, 0, 0.2]), "目标", color="#0b0b0b")
    bx.set(xlabel="x", ylabel="y", zlabel="z", title="平面 W：$z=x+y$")
    bx.set(xlim=(-2, 2), ylim=(-2, 2), zlim=(-4, 4), xticks=[-2, 0, 2], yticks=[-2, 0, 2],
           zticks=[-4, -2, 0, 2, 4])
    bx.view_init(elev=16, azim=-58)
    fig.tight_layout()
    save(fig, "ch09", "dimension-plane.png")


# ---------------------------------------------------------------- 第 10 章
def ch10_grid(name, matrix, title, point_out):
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4))
    for ax, M, ttl, labels in [
        (axes[0], np.eye(2), "输入网格", ("$x_1$", "$x_2$")),
        (axes[1], matrix, title, ("$b_1$", "$b_2$")),
    ]:
        grid_lines(ax, M)
        unit_square(ax, M)
        arrow(ax, (0, 0), M[:, 0], BLUE, lw=3)
        arrow(ax, (0, 0), M[:, 1], ORANGE, lw=2.4)
        p = M @ np.array([2, 1])
        e = M @ np.array([2, 0])
        ax.plot([e[0], p[0]], [e[1], p[1]], color=ORANGE, ls="--", lw=1.6)
        ax.scatter(*p, s=60, color=RED, zorder=5)
        ax.annotate(f"({p[0]:.0f}, {p[1]:.0f})", p, xytext=(8, 8), textcoords="offset points")
        ax.set(xlim=(-5.5, 5.5), ylim=(-3.5, 3.5), aspect="equal", xlabel=labels[0],
               ylabel=labels[1], title=ttl)
        axes_cross(ax)
    handles = [plt.Line2D([], [], color=BLUE, lw=3, label="第一个基向量的去向"),
               plt.Line2D([], [], color=ORANGE, lw=3, label="第二个基向量的去向"),
               plt.Line2D([], [], color=RED, marker="o", lw=0, label="跟踪点 (2, 1)")]
    fig.legend(handles=handles, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.02))
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    save(fig, "ch10", name)


def ch10_figures():
    ch10_grid("shear-grid.png", np.array([[1, 1], [0, 1]]), "输出网格：剪切 A", (3, 1))
    ch10_grid("collapsed-grid.png", np.array([[1, 1], [0, 0]]), "输出网格：B 把平面压成一条线",
              (3, 0))


# ---------------------------------------------------------------- 第 11 章
def ch11_panel(ax, M, title, label_offset=(8, -16)):
    grid_lines(ax, M)
    unit_square(ax, M)
    arrow(ax, (0, 0), M[:, 0], BLUE, lw=2.4)
    arrow(ax, (0, 0), M[:, 1], ORANGE, lw=2.4)
    ax.text(*(M[:, 0] + [0.2, 0.25]), "$e_1$")
    ax.text(*(M[:, 1] + [0.15, 0.3]), "$e_2$")
    p = M @ np.array([2, 1])
    ax.scatter(*p, s=55, color=RED, zorder=5)
    ax.annotate(f"({p[0]:.0f}, {p[1]:.0f})", p, xytext=label_offset, textcoords="offset points")
    ax.set(xlim=(-7, 7), ylim=(-4.5, 4.5), aspect="equal", xlabel="第一坐标",
           ylabel="第二坐标", title=title)
    axes_cross(ax)


def ch11_figures():
    A = np.array([[1, 1], [0, 1]])
    B = np.array([[1, 0], [0, 2]])
    fig, axes = plt.subplots(1, 3, figsize=(13, 3.6))
    ch11_panel(axes[0], np.eye(2), "输入")
    ch11_panel(axes[1], A, "经过 A：剪切")
    ch11_panel(axes[2], B @ A, "再经过 B：竖直拉伸")
    fig.tight_layout()
    save(fig, "ch11", "composition-grid.png")

    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.6))
    ch11_panel(axes[0], B @ A, "先 A 后 B：$BA$")
    ch11_panel(axes[1], A @ B, "先 B 后 A：$AB$")
    fig.tight_layout()
    save(fig, "ch11", "order-comparison.png")


# ---------------------------------------------------------------- 第 12 章
def ch12_inverse():
    S = np.array([[1, 1], [0, 1]])
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.3))
    for ax, M, title in [(axes[0], np.eye(2), "输入"), (axes[1], S, "经过剪切 S"),
                         (axes[2], np.eye(2), "再经过 $R_S$：恢复原样")]:
        grid_lines(ax, M, colors=(BLUE, BLUE), alpha=0.55)
        p = M @ np.array([2, 1])
        ax.scatter(*p, s=55, color=ORANGE, zorder=5)
        ax.annotate(f"({p[0]:.0f}, {p[1]:.0f})", p, xytext=(6, 6), textcoords="offset points")
        ax.set(xlim=(-4.5, 4.5), ylim=(-3, 3), aspect="equal", xlabel="第一坐标",
               ylabel="第二坐标", title=title)
        ax.grid(alpha=0.25)
    fig.tight_layout()
    save(fig, "ch12", "inverse-grid.png")


# ---------------------------------------------------------------- 第 13 章
def ch13_lines():
    fig, ax = plt.subplots(figsize=(5.8, 5.8))
    x = np.linspace(-3, 7, 50)
    ax.plot(x, -x, color=BLUE, lw=2.4, label="$x_1+x_2=0$：零空间")
    ax.plot(x, 5 - x, color=ORANGE, lw=2.4, label="$x_1+x_2=5$：全部解")
    for p, text, off in [((0, 0), "原点", (8, 6)), ((3, 2), "(3, 2)", (-40, -14)),
                         ((4, 1), "(4, 1)", (8, 6)), ((5, 0), "(5, 0)", (8, 6))]:
        ax.scatter(*p, s=40, color="#2b2b29", zorder=5)
        ax.annotate(text, p, xytext=off, textcoords="offset points")
    arrow(ax, (3, 2), (4, 1), RED, lw=2)
    ax.text(3.65, 1.75, "加上 (1, −1)", color="#0b0b0b")
    ax.set(xlim=(-3, 7), ylim=(-3, 7), aspect="equal", xlabel="输入 $x_1$",
           ylabel="输入 $x_2$", title="零调整与全部解：方向相同，位置不同")
    axes_cross(ax)
    ax.legend(loc="upper right", fontsize=10)
    fig.tight_layout()
    save(fig, "ch13", "nullspace-lines.png")


# ---------------------------------------------------------------- 第 14 章
def ch14_rank():
    D = np.array([[1., 1.], [2., 2.]])
    S = np.array([[1., 1.], [1., -1.]])
    values = np.linspace(-2, 2, 9)
    inputs = np.array([(x, y) for x in values for y in values]).T
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))
    for ax, matrix, title, ylabel in [
        (axes[0], D, "重复记录 D：输出只在一条线上，秩 1", "第二项：和的两倍"),
        (axes[1], S, "和与差 S：输出铺满平面，秩 2", "第二项：差"),
    ]:
        outputs = matrix @ inputs
        ax.scatter(*outputs, s=16, color=AQUA, alpha=0.6)
        arrow(ax, (0, 0), matrix[:, 0], BLUE, lw=2.2)
        arrow(ax, (0, 0), matrix[:, 1], ORANGE, lw=2.2)
        ax.set(xlabel="第一项：和", ylabel=ylabel, title=title, xlim=(-5, 5), ylim=(-9, 9))
        axes_cross(ax)
    handles = [plt.Line2D([], [], color=BLUE, lw=2.5, label="第一列"),
               plt.Line2D([], [], color=ORANGE, lw=2.5, label="第二列"),
               plt.Line2D([], [], color=AQUA, marker="o", lw=0, label="部分输入的输出")]
    fig.legend(handles=handles, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.02))
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    save(fig, "ch14", "rank-records.png")


# ---------------------------------------------------------------- 第 18 章
def ch18_work():
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.2))
    for ax, deg in zip(axes, [60, 90, 120]):
        th = np.radians(deg)
        F = np.array([np.cos(th), np.sin(th)]) * 2.2
        ax.axhline(0, color=LIGHT, lw=1.4)
        ax.axvline(0, color=LIGHT, lw=1.4)
        arrow(ax, (0, 0), (3, 0), AQUA, lw=3)
        arrow(ax, (0, 0), F, BLUE, lw=3)
        if deg != 90:
            ax.plot([F[0], F[0]], [0, F[1]], color=GRAY, ls=":", lw=1.4)
            ax.plot([F[0], F[0]], [0, -0.18], color=GRAY, ls=":", lw=1.4)
            ax.plot([0, F[0]], [-0.18, -0.18], color=ORANGE, lw=2.6, ls="--")
        ax.text(F[0], F[1] + 0.25, "F = 10 N", ha="center", color="#0b0b0b")
        ax.text(2.4, -0.45, "d = 3 m", ha="center", color="#0b0b0b")
        W = 10 * 3 * np.cos(th)
        ax.set_title(f"夹角 {deg} 度，功 W = {W:.0f} J".replace("-", "−"))
        ax.set(xlim=(-2, 3.3), ylim=(-0.8, 2.8), aspect="equal")
        ax.axis("off")
    fig.tight_layout()
    save(fig, "ch18", "force-work.png")


# ---------------------------------------------------------------- 第 19 章
def ch19_projection():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10, 4.3))
    c = np.linspace(-1, 4, 200)
    ax.plot(c, (3 - c) ** 2 + (1 - c) ** 2, color=BLUE, lw=2.2)
    ax.scatter([2], [2], s=60, color=RED, zorder=5)
    ax.annotate("c = 2 时最小，误差平方和 2", (2, 2), xytext=(10, 18), textcoords="offset points")
    ax.set(xlabel="两边共同输出的数 $c$", ylabel="误差平方和", title="哪个 $c$ 误差最小")
    ax.grid(alpha=0.25)

    line = np.linspace(-1, 4, 2)
    bx.plot(line, line, color=BLUE, lw=2.2, label="能输出的 $(c,c)$")
    bx.plot([2, 3], [2, 1], color=ORANGE, ls="--", lw=2, label="残差 (1, −1)，与直线垂直")
    bx.scatter([3], [1], s=60, color=RED, zorder=5, label="目标 (3, 1)")
    bx.scatter([2], [2], s=60, color=AQUA, zorder=5, label="最近输出 (2, 2)")
    bx.set(xlim=(-1, 4), ylim=(-1, 4), aspect="equal", xlabel="左声道 L", ylabel="右声道 R",
           title="最近的可达点")
    bx.grid(alpha=0.25)
    bx.legend(loc="upper left", fontsize=9.5)
    fig.tight_layout()
    save(fig, "ch19", "projection.png")


# ---------------------------------------------------------------- 第 20 章
def ch20_fit():
    A = np.array([[80., 1.], [100., 2.], [90., .5]])
    prices = np.array([150., 180., 180.])
    coeffs = np.array([951 / 460, -315 / 23])
    fitted = A @ coeffs
    residual = prices - fitted
    pos = np.arange(3)
    names = ["甲", "乙", "丙"]
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10, 4))
    ax.bar(pos - 0.19, prices, width=0.36, color=BLUE, label="观测价格")
    ax.bar(pos + 0.19, fitted, width=0.36, color=ORANGE, label="共同公式的预测")
    ax.set(xticks=pos, xticklabels=names, ylabel="价格（万元）", ylim=(0, 215),
           title="一组系数同时解释三套房")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(loc="upper left", ncol=2, fontsize=10)
    bx.bar(pos, residual, width=0.55, color=AQUA)
    for p, r in zip(pos, residual):
        bx.text(p, r + (0.4 if r > 0 else -0.4), f"{r:.2f}".replace("-", "−"), ha="center",
                va="bottom" if r > 0 else "top")
    bx.axhline(0, color=GRAY, lw=0.9)
    bx.set(xticks=pos, xticklabels=names, ylabel="观测 − 预测（万元）", ylim=(-5, 5),
           title="残差：都不为零，但都很小")
    bx.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    save(fig, "ch20", "house-fit.png")


# ---------------------------------------------------------------- 第 22 章
def ch22_svd():
    A = np.array([[2., 2.], [-1., 1.]]) / np.sqrt(2)
    V = np.array([[1., -1.], [1., 1.]]) / np.sqrt(2)
    ang = np.linspace(0, 2 * np.pi, 301)
    circle = np.vstack((np.cos(ang), np.sin(ang)))
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.6))
    for ax, M, title in [(axes[0], np.eye(2), "输入：单位圆与两个正交方向"),
                         (axes[1], A, "输出：椭圆，两轴长 2 和 1")]:
        ax.plot(*(M @ circle), color=GRAY, lw=1.6)
        for j, (color, name) in enumerate([(BLUE, "方向 1"), (ORANGE, "方向 2")]):
            vec = M @ V[:, j]
            arrow(ax, (0, 0), vec, color)
            ax.annotate(name, vec, xytext=(6, 6) if j == 0 else (-6, 6),
                        textcoords="offset points", ha="left" if j == 0 else "right")
        ax.set(xlim=(-2.6, 2.6), ylim=(-2.6, 2.6), aspect="equal", xlabel="第一坐标",
               ylabel="第二坐标", title=title)
        axes_cross(ax)
    fig.tight_layout()
    save(fig, "ch22", "svd-directions.png")


# ---------------------------------------------------------------- 第 23 章
def ch23_image():
    rows, cols = np.mgrid[0:112, 0:128]
    image = (.1 + .45 * ((rows > 20) & (rows < 85) & (cols > 25) & (cols < 95))
             + .2 * (np.abs(rows - cols * .8) < 5)
             + .15 * np.sin(rows / 8) * np.cos(cols / 10))
    image = np.clip(image, 0, 1)
    U, s, Vt = np.linalg.svd(image, full_matrices=False)
    fig, axes = plt.subplots(1, 4, figsize=(12, 3.4))
    axes[0].imshow(image, cmap="gray", vmin=0, vmax=1)
    axes[0].set_title("原图")
    for ax, k in zip(axes[1:], [1, 3, 10]):
        approx = (U[:, :k] * s[:k]) @ Vt[:k]
        ax.imshow(np.clip(approx, 0, 1), cmap="gray", vmin=0, vmax=1)
        ax.set_title(f"保留 {k} 项")
    for ax in axes:
        ax.axis("off")
    fig.tight_layout()
    save(fig, "ch23", "low-rank-image.png")


# ---------------------------------------------------------------- 第 24 章
def ch24_pca():
    X = np.array([[2., 1.], [1., 2.], [-1., -2.], [-2., -1.]])
    v = np.array([1., 1.]) / np.sqrt(2)
    proj = (X @ v)[:, None] * v
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10, 4.3))
    line = np.linspace(-2.6, 2.6, 2)
    ax.plot(line, line, color=AQUA, lw=2, label="第一主成分方向")
    for p, q in zip(X, proj):
        ax.plot([p[0], q[0]], [p[1], q[1]], color=ORANGE, ls="--", lw=1.6)
    ax.scatter(*X.T, s=50, color=BLUE, zorder=5, label="中心化后的成绩")
    ax.scatter(*proj.T, s=70, marker="x", color=RED, zorder=6, label="只留一个坐标的重建")
    ax.plot([], [], color=ORANGE, ls="--", label="被删掉的差别")
    ax.set(xlim=(-3, 3), ylim=(-3, 3), aspect="equal", xlabel="第一次测验（减去平均）",
           ylabel="第二次测验（减去平均）", title="共同方向与丢掉的差别")
    axes_cross(ax)
    ax.legend(loc="upper left", fontsize=9)

    bx.bar([0, 1], [0.9, 0.1], width=0.55, color=[BLUE, ORANGE])
    for p, val in zip([0, 1], [0.9, 0.1]):
        bx.text(p, val + 0.02, f"{val:.0%}", ha="center")
    bx.set(xticks=[0, 1], xticklabels=["第一主成分", "第二主成分"], ylim=(0, 1),
           ylabel="方差占比", title="两个方向各解释多少方差")
    bx.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
    bx.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    save(fig, "ch24", "pca-projection.png")


FIGURES = {
    "ch01": ch01_recipe, "ch03": ch03_house, "ch04-displacement": ch04_displacement,
    "ch04-rope": ch04_rope, "ch05": ch05_forces, "ch08": ch08_stereo, "ch09": ch09_plane,
    "ch10": ch10_figures, "ch11": ch11_figures, "ch12": ch12_inverse, "ch13": ch13_lines,
    "ch14": ch14_rank, "ch18": ch18_work, "ch19": ch19_projection, "ch20": ch20_fit,
    "ch22": ch22_svd, "ch23": ch23_image, "ch24": ch24_pca,
}

if __name__ == "__main__":
    for key in sys.argv[1:] or FIGURES:
        FIGURES[key]()
