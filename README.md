# 线性代数如何长出来

从一组方程开始，沿着旧办法遇到的边界，亲手重建矩阵、向量、空间与变换。副标题：从方程的困境到空间、变换与数据。

## 阅读

在线书使用 Hugo + OINK 的 Book 内容模式，支持章节导航、全文搜索、公式、打印视图与移动端阅读。

本地预览：

```bash
hugo server
```

本地环境要求 Git、Go 1.27+ 和 Hugo Extended 0.165.0+。主题作为 Go module 固定在 OINK v1.1.0；无需 Node.js 或 npm。

## 内容结构

- `content/book/`：书籍首页、章节与练习；目录结构就是阅读顺序
- `content/docs/`：学习路线与概念演化图
- `experiments/`：NumPy / Matplotlib 实验源码
- `data/home/zh.yaml`：中文首页内容
- `hugo.yaml`、`go.mod`、`go.sum`：站点与固定版本的主题配置

严格生产构建：

```bash
hugo --cleanDestinationDir --gc --minify --environment production \
  --printPathWarnings --panicOnWarning
```

推送到 `main` 后，GitHub Actions 使用 Hugo Extended 构建并部署到 GitHub Pages。
