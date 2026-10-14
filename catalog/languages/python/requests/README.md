# Requests

> status: draft

## 是什么

Requests 是 Python 事实标准的同步 HTTP 客户端库：API 简洁，适合调用 REST API、下载资源与脚本集成。JetBrains/PSF 开发者调查中长期处于高使用率（与 Web 框架并列统计时常居前列）。

## 何时使用

- 适用：同步脚本与服务中的 HTTP 调用；教学与快速集成。
- 不太适合：需要原生 async、HTTP/2、或与 ASGI 同栈——可优先评估 httpx（见 links）。

## 快速链接

- 官方：https://requests.readthedocs.io/
- 仓库：https://github.com/psf/requests
- 更多见 [links.md](./links.md)

## 本包内容

| 文件 | 说明 |
|------|------|
| [links.md](./links.md) | 外链 |
| [demo/](./demo/) | 最小 GET 示例 |

## 交叉引用

- 主路径：`languages/python/requests`
- 相关：`frameworks/fastapi`、`frameworks/flask`（服务端）；httpx（异步客户端，见 links）
