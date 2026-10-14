# mypy 演示

**可运行**：

```bash
pip install "mypy>=1.8"
cd catalog/languages/python/mypy/demo
mypy example.py
```

[`example.py`](./example.py) 含故意的类型错误，预期 mypy 报错。修正后再次运行应通过。配置片段见 [`mypy.ini`](./mypy.ini)。
