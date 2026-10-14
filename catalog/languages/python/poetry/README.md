# Poetry

> status: draft

## 是什么

Poetry 是 Python 依赖管理与打包工具：用 `pyproject.toml` 声明依赖，生成锁文件，并提供虚拟环境与构建发布流程。标准库 `venv` 仍可用于轻量隔离；Poetry 侧重「项目级」依赖与发布。

## 何时使用

- 适用：应用/库需要可复现依赖、统一的 `add`/`lock`/`build`/`publish` 工作流。
- 不太适合：仅临时脚本、或团队已统一用 [uv](../uv/) 且不想双轨并存。

## 快速链接

- 官方：https://python-poetry.org/
- 仓库：https://github.com/python-poetry/poetry
- 更多见 [links.md](./links.md)

## 本包内容

| 文件 | 说明 |
|------|------|
| [links.md](./links.md) | 外链 |
| [demo/](./demo/) | 初始化与常用命令 |

## 交叉引用

- 主路径：`languages/python/poetry`
- 相关：标准库 `venv`、[pip](../pip/)、[uv](../uv/)
