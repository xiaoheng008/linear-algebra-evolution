# 线性代数：从问题到系统

这是一套从问题出发、逐步重建线性代数的教程。我们不先列定义和公式，而是追问：已有方法遇到了什么困难，什么观察催生了新概念，这个概念又让我们能够提出什么新问题？

教程面向学过基础代数、但不要求有线性代数基础的读者。这里重建的是概念之间的认知路径，不声称复现数学史上的真实先后顺序。

## 从哪里开始

按 [学习路线](docs/SUMMARY.md) 顺序阅读 `docs/book/`。每章会从一个具体问题开始，安排尝试和观察，再给概念命名并严格推导。遇到练习时，建议先写下自己的推理；提示应从最小的一步开始看。

## 目录

- `docs/book/`：教程正文
- `docs/exercises/`：回忆、推导、应用和重建练习
- `docs/experiments/`：可运行的 NumPy / Matplotlib 探索脚本
- `docs/evolution-map.md`：概念依赖与因果压力图

运行实验需要 Python、NumPy 和 Matplotlib。例如：

```bash
python docs/experiments/01_equations.py
```

## 项目状态

当前为 Phase 1：建立从方程、消元到矩阵、向量和线性组合的第一段因果链。后续章节会在这段基础上继续演化。

## 许可

教程文字采用 [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)；实验代码采用 MIT License。详见 [LICENSE](LICENSE)。
