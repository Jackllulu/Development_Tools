# Jupyter 演示

**可运行**：

```bash
pip install "jupyterlab>=4.0"
jupyter lab
# 或经典界面：pip install notebook && jupyter notebook
```

浏览器打开后新建 Python notebook，粘贴：

```python
print(sum(range(10)))
```

[`hello.py`](./hello.py) 为等价脚本，可在 notebook 单元格中复制运行，或直接 `python hello.py`。

> 本目录不提交 `.ipynb` 二进制/大 JSON，以免噪音；以可复制单元格为准。
