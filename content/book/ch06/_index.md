---
title: 哪些向量能由这些列拼出来？
description: 从列向量的线性组合，发现张成与可达输出。
book_number: '6'
weight: 70
---

## 先把刚才的计算倒过来问

第五章里，矩阵的两列是

\[
\mathbf{a}_1=\begin{bmatrix}1\\2\end{bmatrix},\qquad
\mathbf{a}_2=\begin{bmatrix}1\\-1\end{bmatrix}.
\]

输入 `x=(2,3)` 告诉我们各取几倍，输出就是第五章算过的 `b=(5,1)`：

\[
2\mathbf{a}_1+3\mathbf{a}_2=\begin{bmatrix}5\\1\end{bmatrix}.
\]

现在把问题倒过来：给你一个目标向量 `b`，能不能挑出合适的倍数，让这些列拼出 `b`？

## 有些列，够不着整个平面

先换一组更容易看清的列：

\[
\mathbf{u}=\begin{bmatrix}1\\2\end{bmatrix},\qquad
\mathbf{v}=\begin{bmatrix}2\\4\end{bmatrix}.
\]

试几个倍数组合：`u+v=(3,6)`，`−u+v=(1,2)`。都落在同一条直线上。目标 `b=(1,0)` 也能拼出来吗？先别画图，写出任意两个倍数的结果：

\[
c_1\mathbf{u}+c_2\mathbf{v}
=\begin{bmatrix}c_1+2c_2\\2c_1+4c_2\end{bmatrix}.
\]

第二个坐标总是第一个坐标的两倍。所以不论 `c_1,c_2` 怎么选，结果都满足 `y=2x`。`(1,0)` 不满足这条关系，拼不出来。

## 只改一列，再试一次

把第二列的最后一个数从 `4` 改成 `3`：

\[
\mathbf{v}=\begin{bmatrix}2\\3\end{bmatrix}.
\]

现在试试目标 `(1,0)`。取 `−3u+2v`，得到

\[
-3\begin{bmatrix}1\\2\end{bmatrix}
+2\begin{bmatrix}2\\3\end{bmatrix}
=\begin{bmatrix}1\\0\end{bmatrix}.
\]

刚才够不着的目标，现在够到了。不是目标变了，是两列不再指向同一条直线。

而且这次不只 `(1,0)` 能拼出来。任给一个目标 `(p,q)`，我们要解的是

\[
c_1+2c_2=p,\qquad 2c_1+3c_2=q.
\]

第一式乘 2 再减去第二式，得到 `c_2=2p-q`；代回去，`c_1=2q-3p`。无论 `p,q` 是什么实数，都能找到这两个系数。因此这两列可以拼出平面上的任意向量。

## 给所有可能的组合起个名字

给定一组向量，把它们乘上任意实数再相加，所有可能得到的结果放在一起，称为这些向量的**张成**：

\[
\operatorname{span}\{\mathbf{u},\mathbf{v}\}
=\{c_1\mathbf{u}+c_2\mathbf{v}\mid c_1,c_2\in\mathbb{R}\}.
\]

前一组平行的向量张成一条直线；后一组方向不同的向量张成整个平面。`Ax=b` 有没有解，也就有了一个新的说法：`b` 能不能由 `A` 的列组合出来？能，它就在这些列的张成里；不能，方程组就无解。

## 动手改变一列

打开[列向量张成交互实验](https://colab.research.google.com/github/xiaoheng008/linear-algebra-evolution/blob/main/experiments/06_span.ipynb)，先看两列平行时生成的点，再拖动滑块改变第二列的方向。试着让输出落在目标 `(1,0)` 上。若滑块不可用，实验里也有可直接修改参数的静态版本。

也可以下载[实验文件](https://github.com/xiaoheng008/linear-algebra-evolution/blob/main/experiments/06_span.ipynb)在本地运行。

## 下一步：列的描述会不会多余？

现在知道了哪些向量可以由一组列拼出来。但如果有三列，其中一列本来就能由另外两列拼出呢？它带来了新能力，还是只重复了已有信息？下一章从这个问题开始，寻找描述里真正不可少的方向。

## 合上书，自己判断

给出两组二维向量：一组的张成是一条直线，另一组的张成是整个平面。对每组分别说明：任意两个向量的组合有什么形式？给定目标时，你怎样判断它能不能拼出来？
