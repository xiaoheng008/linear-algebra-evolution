---
title: 应用例子
description: 从配料、房价、库存、双声道、报表与图像坐标，读懂方程、矩阵和向量。
weight: 30
---

这些例子与正文一起推进。先看各个量的含义，再手算；最后把结果读回原问题。

| 场景 | 要回答的问题 | 章节 |
|---|---|---|
| 两种原料混合 | 用量怎样同时满足两项成分要求？数学解是否可用？ | [方程组]({{< relref "/book/ch01" >}})、[消元]({{< relref "/book/ch02" >}})、[列组合]({{< relref "/book/ch05" >}})、[张成]({{< relref "/book/ch06" >}}) |
| 假设房价模型 | 怎样由数据找系数，又怎样由系数算另一套房的模型价格？ | [矩阵]({{< relref "/book/ch03" >}})、[两个计算方向]({{< relref "/book/ch05" >}}) |
| 同一距离记录公里和米 | 多一列是否增加信息？系数为什么不唯一？ | [线性相关]({{< relref "/book/ch07" >}}) |
| 仓库库存 | 哪些数可以相加，坐标顺序为什么重要？ | [向量]({{< relref "/book/ch04" >}}) |
| 双声道采样 | 如何混音、产生左右不同的信号、换一种坐标来完整记录？ | [向量]({{< relref "/book/ch04" >}})、[可达范围]({{< relref "/book/ch06" >}})、[基]({{< relref "/book/ch08" >}}) |
| 两渠道销售报表 | 三个字段为何只有两个独立的数？ | [维数]({{< relref "/book/ch09" >}}) |
| 图像特征点 | 剪切与拉伸怎样移动坐标？为什么处理顺序重要？ | [线性变换]({{< relref "/book/ch10" >}})、[矩阵乘法]({{< relref "/book/ch11" >}}) |
| 房价数据换单位 | 怎样把单位换算合进已知系数？ | [矩阵乘法]({{< relref "/book/ch11" >}}) |
| 三种原料、同一成分目标 | 哪些调整不改变产出，怎样写全可用配方？ | [零空间与解集]({{< relref "/book/ch13" >}})、[秩]({{< relref "/book/ch14" >}}) |
| 两平台客户迁移 | 预期人数怎样反复变化，何时趋于稳定？ | [特征方向]({{< relref "/book/ch15" >}})、[对角化]({{< relref "/book/ch17" >}}) |
| 不一致的销售报表 | 什么是最近的一致记录，修改规则怎样影响答案？ | [投影]({{< relref "/book/ch19" >}}) |
| 三套房的冲突观测 | 无精确解时，怎样共同拟合，怎样解释残差？ | [最小二乘]({{< relref "/book/ch20" >}})、[最终重建]({{< relref "/book/ch25" >}}) |
| 灰度数值图像 | 少存几个方向，误差和存储怎样变化？ | [低秩近似]({{< relref "/book/ch23" >}}) |
| 两次测验成绩 | 哪些共同变化值得保留，降维丢掉哪些区别？ | [PCA]({{< relref "/book/ch24" >}}) |

## 可运行的例子

打开[配料与双声道实验](https://colab.research.google.com/github/xiaoheng008/linear-algebra-evolution/blob/main/experiments/application_examples.ipynb)：沿一条成分约束移动配方，观察第二项要求何时满足；再把双声道波形换成共同与差别两个坐标，检查重建与信息丢失。[实验文件](https://github.com/xiaoheng008/linear-algebra-evolution/blob/main/experiments/application_examples.ipynb)可下载到本地运行。

房价与图像坐标分别使用[房价方程实验](https://colab.research.google.com/github/xiaoheng008/linear-algebra-evolution/blob/main/experiments/03_matrix_system.ipynb)、[网格变换实验](https://colab.research.google.com/github/xiaoheng008/linear-algebra-evolution/blob/main/experiments/10_transformations.ipynb)与[变换顺序实验](https://colab.research.google.com/github/xiaoheng008/linear-algebra-evolution/blob/main/experiments/11_composition.ipynb)。
