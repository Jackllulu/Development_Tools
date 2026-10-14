# IPython 演示

**可运行**：

```bash
pip install "ipython>=8.0"
ipython
```

进入后可试：

```python
In [1]: %timeit sum(range(1000))
In [2]: ??dict.get
```

[`snippet.py`](./snippet.py) 可在 IPython 中用 `%run snippet.py` 加载。
