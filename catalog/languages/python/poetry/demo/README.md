# Poetry 演示

**可运行**（需已安装 Poetry）。亦可用标准库对比：

```bash
python -m venv .venv && source .venv/bin/activate
```

## Poetry 最小流程

```bash
poetry new hello-poetry
cd hello-poetry
poetry add requests
poetry run python -c "import requests; print(requests.__version__)"
```

依赖声明见 [`pyproject.snippet.toml`](./pyproject.snippet.toml)。

## 常用命令

```bash
poetry install          # 按锁文件安装
poetry lock             # 更新锁文件
poetry show --tree      # 依赖树
```
