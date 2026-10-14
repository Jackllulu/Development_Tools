# Pydantic

> status: draft

## 是什么

Pydantic 用类型注解做运行时数据校验与序列化：定义模型后自动解析/校验输入，是 FastAPI 等现代栈的核心依赖，也广泛用于配置、API schema 与数据管道边界。

## 何时使用

- 适用：API 请求/响应模型、配置加载、需要清晰校验错误信息的边界层。
- 不太适合：仅编辑器静态检查、无运行时校验需求——可只用 [mypy](../../languages/python/mypy/) / Pyright；极简脚本也可手写 `isinstance`。

## 快速链接

- 官方：https://docs.pydantic.dev/
- 仓库：https://github.com/pydantic/pydantic
- 更多见 [links.md](./links.md)

## 本包内容

| 文件 | 说明 |
|------|------|
| [links.md](./links.md) | 外链 |
| [demo/](./demo/) | 最小模型校验示例 |
| [_index.md](./_index.md) | 分组导航 |

## 交叉引用

- 主路径：`frameworks/pydantic`
- 相关：[FastAPI](../fastapi/)、[SQLAlchemy](../sqlalchemy/)；SQLModel（见 links）
