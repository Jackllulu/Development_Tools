# pip

> status: draft

## 是什么

`pip` 是 Python 官方推荐的包安装器（PyPA），用于从 PyPI 安装、升级与卸载发行包。绝大多数教程与 CI 镜像仍默认提供 `pip`。

## 何时使用

- 适用：快速安装依赖、在已有 `venv` 中管理包、编写 `requirements.txt` 工作流。
- 不太适合：需要确定性锁文件、多环境统一解析、或极快解析安装时——可优先考虑 [uv](../uv/)。

## 快速链接

- 官方文档：https://pip.pypa.io/
- 仓库：https://github.com/pypa/pip
- 更多见 [links.md](./links.md)

## 本包内容

| 文件 | 说明 |
|------|------|
| [links.md](./links.md) | 外链 |
| [demo/](./demo/) | 常用命令与 `requirements.txt` 片段 |

## 交叉引用

- 主路径：`languages/python/pip`
- 相关：[uv](../uv/)、[poetry](../poetry/)
