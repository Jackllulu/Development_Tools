# 贡献指南

感谢参与 **Development Tools** 目录建设。本文说明如何新增或完善一个工具条目。

本仓库是 **GitHub 上的 Markdown + 示例目录**：在仓库内维护分类条目、链接与 `demo/` 实现样例。不建设独立开放网站。

---

## 快速开始

1. Fork / 检出仓库，基于默认分支创建主题分支。
2. 复制模板：

```bash
# 示例：在 Python 语言下新增 poetry
cp -R templates/tool catalog/languages/python/poetry
```

3. 编辑 `meta.yaml` 与 `README.md`，按需填写其余文件（含 `demo/`）。
4. 将 `status` 设为合适值（新建多为 `stub` 或 `draft`）。
5. 更新相关 `_index.md`（可选但推荐）。
6. 提交 PR，说明工具是什么、为何收录、主路径为何选该维度。

---

## 选路径

| 问题 | 倾向 |
|------|------|
| 是否主要服务某一语言生态？ | `catalog/languages/<lang>/<tool>/` |
| 是否强绑定某框架？ | `catalog/frameworks/<framework>/<tool>/` |
| 是否跨语言、按场景选型？ | `catalog/domains/<domain>/<tool>/` |

拿不准时选**使用者最常检索的维度**作为主路径，并在 `README.md` 注明其他关联生态。

---

## PR 期望

- 小而清晰：一次 PR 一个工具，或同一分组下少数相关 stub。
- 遵守 [内容规范](./content-standards.md)。
- 不顺带重构无关目录；**不要新增站点工程**（Astro / VitePress 等）。
- 标题示例：`catalog: add ruff under languages/python`。

---

## 完善已有条目

- 升格 `stub` → `draft` → `ready` 时，在 PR 中写明补了哪些面（analysis / usage / demo / links）。
- 修正死链、过时命令时，更新 `meta.yaml` 的 `updated`。

---

## 文档与架构

- 改分类法或包形态前，先读并更新 [项目架构](./project-architecture.md)。
- 批量录入或补演示前读 [开发前准备](./pre-dev-prep.md)。
