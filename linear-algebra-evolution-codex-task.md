# 任务：构建《线性代数：从问题到系统》

你现在负责在本地 Git 仓库中完成一个长期项目：

> **linear-algebra-evolution**

目标是构建一本 Markdown 形式的“演化式线性代数教程”。

---

## 一、项目核心思想

不要把线性代数当成一套已经完成的知识点来讲。

传统方式：

```text
定义
↓
定理
↓
公式
↓
例题
↓
习题
```

本项目采用：

```text
问题
↓
尝试
↓
现有方法遇到瓶颈
↓
发现新的结构
↓
抽象出新的概念
↓
获得新的能力
↓
产生更复杂的问题
↓
继续演化
```

最终希望读者获得的不是：

> “我记住了矩阵、特征值、SVD。”

而是：

> “我理解为什么这些概念会一个接一个出现。”

甚至在忘记公式之后，也能够根据问题重新构建这些概念。

---

# 二、核心教学循环

每一章尽量遵循：

```text
Problem
↓
Try
↓
Failure
↓
Discovery
↓
Concept
↓
Derivation
↓
Experiment
↓
Visualization
↓
Connection
↓
Reconstruction
```

其中最重要的是：

### Problem

先给出真实的问题。

### Try

鼓励读者自己尝试。

### Failure

明确指出旧方法为什么开始不够用了。

### Discovery

让新结构从问题中自然出现。

### Concept

这时才正式命名数学概念。

### Derivation

从已经知道的东西推导公式，而不是直接告诉公式。

### Experiment

尽可能使用 Python / NumPy 做实验。

### Visualization

能画图时就画图。

### Connection

把新概念连接到之前已经建立的结构。

### Reconstruction

要求读者合上书重新推导。

---

# 三、整体知识演化路线

最终教程规划为：

```text
线性方程
  ↓
消元
  ↓
矩阵
  ↓
向量
  ↓
线性组合
  ↓
张成
  ↓
线性无关
  ↓
基
  ↓
维数
  ↓
线性变换
  ↓
矩阵乘法
  ↓
逆矩阵
  ↓
列空间
  ↓
零空间
  ↓
秩
  ↓
秩-零化度
  ↓
特征向量
  ↓
特征值
  ↓
对角化
  ↓
距离
  ↓
正交
  ↓
投影
  ↓
最小二乘
  ↓
特征分解的局限
  ↓
SVD
  ↓
降维
  ↓
数据
  ↓
统一视角
  ↓
最终重建
```

注意：

这不是简单的知识点目录。

必须保证每一步都是前一步产生的新问题推动出来的。

---

# 四、章节规划

创建：

```text
book/
```

并规划以下章节：

```text
00-preface.md
01-linear-equations.md
02-elimination.md
03-matrix.md
04-vector.md
05-linear-combination.md
06-span.md
07-independence.md
08-basis.md
09-dimension.md
10-linear-transformation.md
11-matrix-multiplication.md
12-inverse.md
13-column-space.md
14-null-space.md
15-rank.md
16-rank-nullity.md
17-eigenvector.md
18-eigenvalue.md
19-diagonalization.md
20-distance.md
21-orthogonality.md
22-projection.md
23-least-squares.md
24-from-eigen-to-svd.md
25-svd.md
26-svd-dimensionality-reduction.md
27-svd-data.md
28-unification.md
29-reconstruction.md
30-final-reconstruction.md
```

同时创建：

```text
README.md
SUMMARY.md
LICENSE

exercises/
experiments/
```

---

# 五、重要教学原则

## 1. 不要提前泄露答案

例如讲线性组合之前，不要突然告诉读者：

> “矩阵乘法其实就是列向量的线性组合。”

应该让读者先计算：

```text
Ax
```

然后观察：

```text
Ax =
x₁a₁ + x₂a₂ + ... + xₙaₙ
```

最后才发现：

> 原来矩阵乘向量就是在组合矩阵的列。

---

## 2. 不要把概念当作定义背诵

例如：

不要直接：

> 向量组线性无关，当且仅当……

而应该先制造问题：

> 如果一个向量可以由其他向量表示，那么我们是不是重复保存了信息？

然后逐渐产生：

```text
冗余
↓
依赖
↓
线性依赖
↓
线性无关
```

---

## 3. 每一个抽象都必须有“压力来源”

如果引入一个新概念，必须回答：

> **如果没有这个概念，之前的问题为什么越来越难？**

例如：

```text
矩阵
```

解决的是大量方程的统一表示。

```text
向量
```

解决的是把多个相关量作为整体处理。

```text
线性组合
```

解决的是理解 Ax 到底在做什么。

```text
基
```

解决的是寻找一组最小但足够的描述方式。

```text
维数
```

解决的是衡量一个空间需要多少独立方向。

---

# 六、数学严谨性

虽然采用探索式叙事，但最终数学必须严格。

要求：

- 所有公式正确
- 推导不能跳过关键逻辑
- 例子必须可验证
- 符号定义明确
- 不偷换概念
- 不为了故事牺牲数学准确性

如果直觉解释与严格定义存在差异，要明确区分：

```text
直觉
严格定义
```

---

# 七、实验系统

创建：

```text
experiments/
```

实验使用 Python + NumPy + Matplotlib。

例如：

```text
experiments/
├── 01_equations.py
├── 02_elimination.py
├── 03_matrix_transformation.py
├── ...
```

实验的目标不是为了展示代码，而是：

> **让读者通过实验观察数学结构。**

例如：

- 改变矩阵
- 观察二维空间中的变换
- 观察向量张成
- 观察线性相关
- 观察投影
- 观察最小二乘
- 观察特征向量
- 观察 SVD

---

# 八、习题系统

创建：

```text
exercises/
```

习题不要全部设计成计算题。

至少包含四种：

### Recall

检查是否理解概念。

### Derivation

要求从已有知识重新推导。

### Application

把概念用于新问题。

### Reconstruction

不给公式，让读者重新建立概念。

例如：

> 你忘记了投影公式，只知道“投影应该是目标方向上的某个倍数”。请从这个事实重新推出公式。

这种题比单纯计算更重要。

---

# 九、阶段性目标

不要一开始把 30 章全部写满。

采用迭代方式。

## Phase 1

完成：

```text
README
SUMMARY
00-preface
01-linear-equations
02-elimination
03-matrix
04-vector
05-linear-combination
```

并检查这六章是否形成真正的因果链。

## Phase 2

完成：

```text
06-span
07-independence
08-basis
09-dimension
10-linear-transformation
11-matrix-multiplication
12-inverse
```

## Phase 3

完成：

```text
13-column-space
14-null-space
15-rank
16-rank-nullity
```

## Phase 4

完成：

```text
17-eigenvector
18-eigenvalue
19-diagonalization
```

## Phase 5

完成：

```text
20-distance
21-orthogonality
22-projection
23-least-squares
```

## Phase 6

完成：

```text
24-from-eigen-to-svd
25-svd
26-svd-dimensionality-reduction
27-svd-data
```

## Phase 7

完成：

```text
28-unification
29-reconstruction
30-final-reconstruction
```

---

# 十、工作方式

现在不要直接写完整 30 章。

首先：

1. 检查当前仓库
2. 阅读已有文件
3. 分析当前结构
4. 创建项目骨架
5. 完成 Phase 1
6. 运行 Markdown / 链接 / Python 实验检查
7. 检查数学推导
8. 查看 git diff
9. 创建 commit

Commit message 使用：

```text
build: establish evolutionary linear algebra tutorial foundation
```

不要在没有检查的情况下大量生成内容。

---

# 十一、最重要的质量标准

最终判断本项目是否成功，不是看：

> 写了多少章节。

而是看：

> **一个初学者是否能够沿着教程的因果链，自己重新发现线性代数。**

理想情况下，读者学完之后应该能够从：

```text
我有一个问题
```

一路重新构建：

```text
方程
→ 矩阵
→ 向量
→ 线性组合
→ 空间
→ 基
→ 变换
→ 特征结构
→ 正交
→ 投影
→ SVD
```

因此，请始终优先保证：

**因果关系 > 知识覆盖率**

**理解 > 记忆**

**推导 > 背公式**

**重建能力 > 做标准题**

现在开始执行 Phase 1。
