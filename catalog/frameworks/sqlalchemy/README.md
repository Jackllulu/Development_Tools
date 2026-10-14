# SQLAlchemy

> status: draft

## 是什么

SQLAlchemy 是 Python 最常用的 SQL 工具包与 ORM：既可写 Core（表达式/连接）也可写 ORM 映射，广泛用于 Flask / FastAPI 等栈的数据访问层。

## 何时使用

- 适用：需要灵活 SQL 控制或跨库 ORM；与 Web 框架解耦的数据层。
- 不太适合：只要 Django 全家桶——Django ORM 通常够用；极简一次性脚本可直接用 DB API。

## 快速链接

- 官方：https://www.sqlalchemy.org/
- 文档：https://docs.sqlalchemy.org/
- 仓库：https://github.com/sqlalchemy/sqlalchemy
- 更多见 [links.md](./links.md)

## 本包内容

| 文件 | 说明 |
|------|------|
| [links.md](./links.md) | 外链 |
| [demo/](./demo/) | 内存 SQLite 最小 ORM 示例 |
| [_index.md](./_index.md) | 分组导航 |

## 交叉引用

- 主路径：`frameworks/sqlalchemy`
- 相关：[FastAPI](../fastapi/)、[Flask](../flask/)、[Django](../django/)（自带 ORM）
