# mypy

> status: draft

## 是什么

mypy 是主流的 Python 静态类型检查器：在不运行代码的情况下根据类型注解发现接口错误，可与 `typing` / `py.typed` 库配合渐进采用。

## 何时使用

- 适用：中大型代码库希望尽早发现类型错误；库作者提供类型信息。
- 不太适合：纯脚本且无类型注解、又不打算引入注解时——收益有限。

## 快速链接

- 官方：https://mypy.readthedocs.io/
- 仓库：https://github.com/python/mypy
- 更多见 [links.md](./links.md)

## 本包内容

| 文件 | 说明 |
|------|------|
| [links.md](./links.md) | 外链 |
| [demo/](./demo/) | 故意含类型错误的最小示例 |

## 交叉引用

- 主路径：`languages/python/mypy`
- 相关：[ruff](../ruff/)、[pytest](../pytest/)
