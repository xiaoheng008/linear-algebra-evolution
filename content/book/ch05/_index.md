---
title: 矩阵乘向量的输出由什么组成？
description: 从矩阵乘法的坐标展开中发现线性组合。
book_number: '5'
weight: 60
---

## 起点：算出输出还不够，要看输入如何参与

对矩阵和输入

\[
A=\begin{bmatrix}1&2\\3&1\end{bmatrix},\qquad
\mathbf{x}=\begin{bmatrix}4\\-1\end{bmatrix},
\]

计算 `A x`。我们希望不只得到数字，还理解输入的两个坐标怎样共同决定输出。

## 先按行计算，再按输入坐标重新分组

先只算输出的第一个坐标。矩阵第一行与输入做什么运算？

> [!DETAILS] 第一个坐标
> `1·4+2·(−1)=2`。先把这个结果记下来，不急着概括。

再看第二行：同样的规则会给出什么？

> [!DETAILS] 第二个坐标
> `3·4+1·(−1)=11`。所以 `A x=[2,11]^T`。

现在停一下：每个输出坐标是用矩阵的“行”算出来的。但输入中的 `4` 和 `−1`，分别乘上了矩阵的哪些数字？试着按输入坐标重新分组：

> [!DETAILS] 把乘法重新排一排
> \[
> A\mathbf{x}=4\begin{bmatrix}1\\3\end{bmatrix}+(-1)\begin{bmatrix}2\\1\end{bmatrix}
> =\begin{bmatrix}4\\12\end{bmatrix}+\begin{bmatrix}-2\\-1\end{bmatrix}
> =\begin{bmatrix}2\\11\end{bmatrix}.
> \]
> `4` 乘第一列，`−1` 乘第二列；两列相加后，回到刚才按行算出的同一个输出。

## 关键观察：每个输入坐标控制矩阵的一列

右侧出现了矩阵的两列。输入第一个坐标决定第一列取多少倍，第二个坐标决定第二列取多少倍，再把结果相加。按行看，是每个输出坐标如何计算；按列看，是输入如何组合出整个输出。

## 命名：线性组合

向量 `v_1,...,v_k` 的线性组合，是形如 `c_1v_1+...+c_kv_k` 的向量，其中 `c_i` 为标量。本例中

\[
A\mathbf{x}=x_1\mathbf{a}_1+x_2\mathbf{a}_2,
\]

其中 `a_1,a_2` 是 `A` 的列。这个等式由矩阵乘法逐坐标展开得到，不是额外假设。

## 能力升级：把矩阵乘法读成可达输出的生成规则

设 `A` 的列为 `a_1,...,a_n`，即 `A=[a_1 ... a_n]`，输入为 `x=[x_1,...,x_n]^T`。矩阵乘法按行定义：第 `i` 个输出坐标为 `sum_j A_ij x_j`。而向量 `sum_j x_j a_j` 的第 `i` 个坐标也是 `sum_j x_j (a_j)_i=sum_j x_j A_ij`。每个坐标相等，因此

\[
A\mathbf{x}=\sum_{j=1}^n x_j\mathbf{a}_j.
\]

## 实验

打开[列组合 Notebook](https://colab.research.google.com/github/xiaoheng008/linear-algebra-evolution/blob/main/experiments/05_column_combination.ipynb)，先手算，再用滑块改变输入坐标，观察矩阵的列如何组合成输出；Notebook 也可下载到本地运行。

## 新问题：所有可能的输出究竟构成什么？

线性组合提供了理解 `Ax` 的新视角：固定矩阵的列，输入改变时，输出在这些列所能组合出的范围内变化。下一步自然是问：究竟哪些向量能由给定列组合得到？这将引出张成。

## 重建

从矩阵乘法的按行定义出发，逐坐标推导 `Ax=sum_j x_j a_j`。再解释：为什么这个等式能帮助我们判断方程 `Ax=b` 是否有解？
