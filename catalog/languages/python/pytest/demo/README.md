# pytest 演示

**可运行**最小示例。

```bash
cd catalog/languages/python/pytest/demo
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

预期：`test_add.py` 中 2 个用例通过。

源码：[`test_add.py`](./test_add.py)、[`requirements.txt`](./requirements.txt)。
