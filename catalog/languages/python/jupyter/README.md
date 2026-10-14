# Jupyter

> status: draft

## 是什么

Jupyter 生态（Notebook / JupyterLab）提供基于浏览器的交互式计算：代码、叙述与可视化同页呈现，广泛用于数据探索、教学与实验记录。内核常基于 [IPython](../ipython/)。

## 何时使用

- 适用：探索性分析、演示与教学、可复现实验草稿。
- 不太适合：大型生产服务代码的主工程结构——宜把稳定逻辑抽到模块并用 [pytest](../pytest/) 测试。

## 快速链接

- 官方：https://jupyter.org/
- 文档：https://docs.jupyter.org/
- 仓库（Notebook）：https://github.com/jupyter/notebook
- 更多见 [links.md](./links.md)

## 本包内容

| 文件 | 说明 |
|------|------|
| [links.md](./links.md) | 外链 |
| [demo/](./demo/) | 安装启动与最小 notebook 说明 |

## 交叉引用

- 主路径：`languages/python/jupyter`
- 相关：[ipython](../ipython/)
- 领域：亦可交叉参考 `domains/data`、`domains/ai-ml`（占位）
