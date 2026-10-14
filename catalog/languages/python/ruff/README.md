# Ruff

> status: draft

## 是什么

Ruff 是 Astral 出品的极速 Python linter（并可格式化）：用单一工具覆盖大量 Flake8/isort 类规则，配置集中在 `pyproject.toml` 或 `ruff.toml`。

## 何时使用

- 适用：希望 CI/本地秒级反馈；新项目统一 lint + format。
- 不太适合：已深度定制 Black + 多插件且短期不想迁移——可并存或逐步替换 [black](../black/)。

## 快速链接

- 官方：https://docs.astral.sh/ruff/
- 仓库：https://github.com/astral-sh/ruff
- 更多见 [links.md](./links.md)

## 本包内容

| 文件 | 说明 |
|------|------|
| [links.md](./links.md) | 外链 |
| [demo/](./demo/) | 配置片段与检查命令 |

## 交叉引用

- 主路径：`languages/python/ruff`
- 相关：[black](../black/)、[uv](../uv/)、[mypy](../mypy/)
