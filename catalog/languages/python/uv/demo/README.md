# uv 演示

**可运行**（需先安装 `uv`）。安装方式见官方文档；常见：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 最小项目流程

```bash
mkdir hello-uv && cd hello-uv
uv init
uv add requests
uv run python -c "import requests; print(requests.__version__)"
```

同目录 [`pyproject.snippet.toml`](./pyproject.snippet.toml) 展示依赖片段，可复制进 `pyproject.toml` 的 `[project]` 段参考。

## 常用命令

```bash
uv sync          # 按锁文件同步环境
uv pip install X # 兼容 pip 风格的安装接口
uv python list   # 查看可管理的 Python 版本
```
