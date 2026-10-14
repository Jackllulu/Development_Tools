# pre-commit

> status: draft

## 是什么

pre-commit 是基于 Git hook 的代码质量门禁框架：在提交前自动跑 Ruff、mypy、格式化等检查，配置集中在 `.pre-commit-config.yaml`，广泛出现在现代 Python 项目模板与 CI 前置流程中。

## 何时使用

- 适用：希望本地在 push/CI 之前就拦住 lint/format 问题；多工具统一用一套 hook。
- 不太适合：个人一次性脚本、或不想引入 Git hook 的极简仓库——可直接在 CI 跑同等命令。

## 快速链接

- 官方：https://pre-commit.com/
- 仓库：https://github.com/pre-commit/pre-commit
- 更多见 [links.md](./links.md)

## 本包内容

| 文件 | 说明 |
|------|------|
| [links.md](./links.md) | 外链 |
| [demo/](./demo/) | 最小配置片段与安装命令 |

## 交叉引用

- 主路径：`languages/python/pre-commit`
- 相关：[ruff](../ruff/)、[black](../black/)、[mypy](../mypy/)
