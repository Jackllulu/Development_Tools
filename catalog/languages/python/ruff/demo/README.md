# Ruff 演示

**可运行**（需已安装 `ruff`，例如 `pip install ruff`）。

```bash
cd catalog/languages/python/ruff/demo
ruff check .
ruff format --check .
# 自动修复 / 格式化：
# ruff check --fix .
# ruff format .
```

样例源码 [`sample.py`](./sample.py) 含可被检查的风格问题；配置见 [`ruff.toml`](./ruff.toml)。
