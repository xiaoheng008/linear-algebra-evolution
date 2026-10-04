---
title: 矩阵乘向量的输出由什么组成？
description: 从同一组方程的两种读法，发现矩阵乘法是列向量的线性组合。
book_number: '5'
weight: 60
---

## 回到第一章的交点

第一章解过这组方程：

\[
\begin{cases}
x+y=5,\\
2x-y=1.
\end{cases}
\]

当右边的数是 5 和 1 时，两条直线交于 `(2,3)`。当时我们从方程出发找交点。现在反过来：若已知点 `(2,3)`，把它代进每条方程，右边会得到什么？

\[
2+3=5,\qquad 2\cdot2-3=1.
\]

每一行各算出一个数，按顺序排起来就是 `b=(5,1)`。这一次是给定 `x`，逐行算出 `b`；第一章则是给定 `b`，找出同时满足两行的 `x`。

![两条直线 x+y=5 与 2x-y=1 相交于 (2,3)；把交点代入两行，分别得到 b 的坐标 5 和 1](ax-b-directions.svg)

## 把两行写成矩阵

把每行中 `x`、`y` 的系数排在一起：

\[
A=\begin{bmatrix}1&1\\2&-1\end{bmatrix},\qquad
\mathbf{x}=\begin{bmatrix}2\\3\end{bmatrix},\qquad
\mathbf{b}=\begin{bmatrix}5\\1\end{bmatrix}.
\]

按行计算，第一行给出 `1·2+1·3=5`，第二行给出 `2·2−1·3=1`。所以

\[
A\mathbf{x}=\begin{bmatrix}1&1\\2&-1\end{bmatrix}
\begin{bmatrix}2\\3\end{bmatrix}
=\begin{bmatrix}5\\1\end{bmatrix}=\mathbf{b}.
\]

这里的 `b` 是计算结果，不是预先指定的目标。

## 同一次计算，按列重排

刚才按行看，每一行各算一个输出。现在按输入中的数重新分组。把 `x` 的第一项 2 与矩阵第一列相乘，把第二项 3 与第二列相乘，再把两列相加：

\[
2\begin{bmatrix}1\\2\end{bmatrix}
+3\begin{bmatrix}1\\-1\end{bmatrix}
=\begin{bmatrix}2\\4\end{bmatrix}
+\begin{bmatrix}3\\-3\end{bmatrix}
=\begin{bmatrix}5\\1\end{bmatrix}.
\]

得到的还是刚才的 `b`。输入 `x` 的坐标，恰好是矩阵各列要乘的倍数。按行分组容易算出每个输出坐标；按列分组则让我们看见：输入怎样把各列组合成输出。

## 这叫线性组合

把若干向量各乘一个数，再把结果相加，叫作它们的**线性组合**。本例中，`A` 的两列是

\[
\mathbf{a}_1=\begin{bmatrix}1\\2\end{bmatrix},\qquad
\mathbf{a}_2=\begin{bmatrix}1\\-1\end{bmatrix},
\]

因此 `A x = 2a_1+3a_2=b`。这不是另一条矩阵乘法规则，而是把按行展开的乘法重新分组。

若矩阵有 `n` 列，把第 `i` 个输出坐标展开，就能核对一般情形：

\[
(A\mathbf{x})_i=\sum_{j=1}^n A_{ij}x_j.
\]

矩阵第 `j` 列在第 `i` 个位置的数正是 `A_ij`，所以各列按 `x_j` 倍相加后，第 `i` 个坐标仍是这个和。每个坐标都相同，便有

\[
A\mathbf{x}=\sum_{j=1}^n x_j\mathbf{a}_j.
\]

## 已知哪一边，决定要做哪件事

`A x=b` 可以提出两个方向的问题。已知 `A` 和 `x`，按行计算就得到 `b`；已知 `A` 和目标 `b`，则要找出能组成这个目标的输入 `x`。后者正是解方程组：每个目标坐标都给出一条约束，答案必须同时满足它们。

所以“根据 `A` 和给定的 `x` 求 `b`”并不是另一种解方程。它是在执行矩阵规定的计算；反过来求 `x`，才是在问哪些输入会产生指定输出。

## 实验

打开[列组合交互实验](https://colab.research.google.com/github/xiaoheng008/linear-algebra-evolution/blob/main/experiments/05_column_combination.ipynb)，先按 Notebook 给出的矩阵和输入，分别用行、列两种方式手算输出，再运行代码核对。随后改变输入，观察列的倍数变了，输出怎样跟着变。也可以下载[实验文件](https://github.com/xiaoheng008/linear-algebra-evolution/blob/main/experiments/05_column_combination.ipynb)在本地运行。

## 下一步：这些列一共能生成哪些输出？

输入改变时，输出仍是这两列的某种组合。哪些目标能这样得到，哪些够不着？下一章就来找出这批可能输出的范围。

## 不看推导，重新分组一次

从 `A x` 的按行计算出发，自己把各项按 `x` 的坐标重新分组，说明为什么结果等于矩阵列的加权和。再回答：已知 `A,x` 与已知 `A,b`，分别要找什么？
