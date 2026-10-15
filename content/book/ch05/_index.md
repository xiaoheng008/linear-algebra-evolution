---
title: 矩阵乘向量的输出由什么组成？
linkTitle: '列组合：输出由各列拼成'
description: 从混合原料的成分计算出发，按行、按列读同一次计算，再用绳索受力迁移并推导一般公式。
book_number: '5'
weight: 60
---

## 我们已经会按行算，再看一次每列

成分表为

\[
A=\begin{bmatrix}10&20\\20&10\end{bmatrix}.
\]

用量 \((1,2)^T\) 产生

\[
A\begin{bmatrix}1\\2\end{bmatrix}
=\begin{bmatrix}10\cdot1+20\cdot2\\20\cdot1+10\cdot2\end{bmatrix}
=\begin{bmatrix}50\\40\end{bmatrix}.
\]

按行算，分别回答蛋白质和脂肪有多少。不过我们取原料时，不是先取蛋白质，再取脂肪：一份甲带来两项，一份乙也带来两项。这个动作更适合按列读。

## 一列就是一整份贡献

甲、乙每份的完整成分正是两列：

\[
\mathbf a_1=\begin{bmatrix}10\\20\end{bmatrix},\qquad
\mathbf a_2=\begin{bmatrix}20\\10\end{bmatrix}.
\]

一份甲、两份乙，就是先把第二列放大两倍，再整列相加：

\[
\mathbf a_1+2\mathbf a_2
=\begin{bmatrix}10\\20\end{bmatrix}+\begin{bmatrix}40\\20\end{bmatrix}
=\begin{bmatrix}50\\40\end{bmatrix}.
\]

结果当然应该相同，因为我们没有改原料，只改变了合并顺序。按行是在算每项总量，按列是在合并每种原料的贡献。

若用量改成 \((2,1)^T\)，先想整份贡献会怎样换，再核对：得到 \(2\mathbf a_1+\mathbf a_2=(40,50)^T\)。这也说明输入的第一项究竟负责什么：它不是输出第一项，而是**第一列取多少倍**。

## 把这个读法写成任意用量

用量是 \(x,y\) 时，两项总成分可以重新分组为

\[
A\begin{bmatrix}x\\y\end{bmatrix}
=x\begin{bmatrix}10\\20\end{bmatrix}
+y\begin{bmatrix}20\\10\end{bmatrix}.
\]

若有更多列，道理也一样。用第三章的记号，\(a_{ij}\) 是第 \(i\) 行、第 \(j\) 列的数。只看输出的第 \(i\) 个坐标，按行得到 \(\sum_ja_{ij}x_j\)。符号 \(\sum\) 读作“求和”，这里表示把 \(j=1,2,\ldots,n\) 的各项 \(a_{ij}x_j\) 全部加起来。

按列算呢？第 \(j\) 列的第 \(i\) 项正是 \(a_{ij}\)，取 \(x_j\) 倍后变成 \(a_{ij}x_j\)；各列相加，第 \(i\) 项还是同一个和。每个坐标都相同，所以

\[
A\mathbf x=\sum_{j=1}^n x_j\mathbf a_j.
\]

这条公式不是需要另外接受的乘法规则，而是原规则的重新分组。把若干向量分别乘一个数再相加，叫它们的**线性组合**。

## 已知用量，和找用量，是同一个关系的两面

给定 \(\mathbf x\)，\(A\mathbf x\) 算它能产生的结果。给定目标 \(\mathbf b\)，求 \(A\mathbf x=\mathbf b\)，就是找每列取几倍才能拼出目标。

第一章把它看成各行约束的交集；现在按列看，则是各份贡献的组合。两个视角在回答同一个问题，不是两套互不相干的理论。

## 力的合成也能按列读

左、右绳每 1 牛顿张力的方向是 \((-0.6,0.8)^T\)、\((0.6,0.8)^T\)。把它们排成矩阵的两列：

\[
F=\begin{bmatrix}-0.6&0.6\\0.8&0.8\end{bmatrix}.
\]

输入是两根绳的张力 \((T_L,T_R)^T\)，输出是两绳的合力。按列读，\(F(T_L,T_R)^T=T_L\cdot\text{左列}+T_R\cdot\text{右列}\)：输入的两个数分别决定每根绳出多少力。

上一章各拉 50 牛顿，两边一样大，水平方向正好抵消。现在不对称地拉：左绳 25 牛顿，右绳 75 牛顿：

\[
25\begin{bmatrix}-0.6\\0.8\end{bmatrix}
+75\begin{bmatrix}0.6\\0.8\end{bmatrix}
=\begin{bmatrix}-15+45\\20+60\end{bmatrix}
=\begin{bmatrix}30\\80\end{bmatrix}.
\]

竖直方向仍是 80 牛顿，因为两绳竖直分量的比例相同，总张力也还是 100 牛顿。水平方向却不再抵消：右列取得多，合力就偏向右边 30 牛顿。再加上重力 \((0,-80)\)，还剩 \((30,0)\)：竖直方向平衡了，水平方向没有，重物会被往右拉动。

![左图：张力各 50 牛顿时两力首尾相接，合力 (0,80) 竖直向上；右图：左 25、右 75 牛顿时，合力 (30,80) 偏向右侧](force-combination.png)

两幅图都把两个力首尾相接：先画左绳的力，再从它的终点画右绳的力。哪一列取得多，合力就偏向哪一边。

数学上的线性组合允许任意实数系数，而配料用量、绳索张力都不能为负。接下来先研究所有实数组合，再回到实际问题筛选；这样能分清一个限制是来自列本身，还是来自“不能为负”。

## 不借背景也读得懂吗？

取 \(A=\begin{bmatrix}1&1\\2&-1\end{bmatrix}\)、输入 \((2,3)^T\)。不直接逐行算，先写成两列的组合。

> [!DETAILS] 核对
> \(2(1,2)^T+3(1,-1)^T=(5,1)^T\)。逐行也得到 \((2+3,4-3)^T\)。输入有两项，分别控制两列，而不是分别控制输出的两项。

[列组合实验](https://colab.research.google.com/github/xiaoheng008/linear-algebra-evolution/blob/main/experiments/05_column_combination.ipynb)让你分别改变两个输入；[配料实验](https://colab.research.google.com/github/xiaoheng008/linear-algebra-evolution/blob/main/experiments/application_examples.ipynb)和[绳索实验](https://colab.research.google.com/github/xiaoheng008/linear-algebra-evolution/blob/main/experiments/physics_forces.ipynb)把每列重新读回实际贡献。

这也留下一个新疑问：我们已经能拼出 \((50,40)\)，但是否每个目标都能这样拼？如果某个目标拼不出，是用量没选好，还是这些列本身不够？下一章要把这两种情况分清。
