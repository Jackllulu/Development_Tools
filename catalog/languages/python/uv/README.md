# uv

> status: draft

## 是什么

`uv` 是 Astral 出品的极速 Python 包与项目管理工具：可替代常见的 `pip` + `venv` + `pip-tools`/`poetry` 工作流（安装、锁文件、虚拟环境、脚本运行）。

## 何时使用

- 适用：新项目希望更快的依赖解析与安装；需要统一的 `uv sync` / `uv run` 体验。
- 不太适合：团队规范强制仅用 Poetry/pip 且暂不引入新工具时——可先读官方迁移说明。

## 快速链接

- 官方：https://docs.astral.sh/uv/
- 仓库：https://github.com/astral-sh/uv
- 更多见 [links.md](./links.md)

## 本包内容

| 文件 | 说明 |
|------|------|
| [links.md](./links.md) | 外链 |
| [demo/](./demo/) | 初始化与同步的最小命令 |

## 交叉引用

- 主路径：`languages/python/uv`
- 相关：[pip](../pip/)、[poetry](../poetry/)、[ruff](../ruff/)（同属 Astral）
