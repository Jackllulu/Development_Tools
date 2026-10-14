# Black 演示

**可运行**：

```bash
pip install "black>=24.0"
cd catalog/languages/python/black/demo
black --check unformatted.py
black unformatted.py   # 就地格式化
```

[`unformatted.py`](./unformatted.py) 为故意未格式化的片段，便于观察 Black 行为。
