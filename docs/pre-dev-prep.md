# 开发前准备（Pre-development Preparation）

在批量录入工具内容或编写实现样例之前，先对齐目标、内容规范与本地环境。读完本文并勾选文末清单后再开工。

---

## 1. 目标与范围

### 1.1 目标

- 维护一份托管在 **GitHub 的开源工具目录**（语言 / 框架 / 领域）。
- 每个工具具备：**分类归属、外链、仓库内实现样例**（可运行或可复制粘贴）。
- 浏览方式：在 GitHub 上打开 `README.md` 与 `catalog/` 下各级 `_index.md`；本地则 `git clone` 后按同样树状结构阅读与运行 demo。

### 1.2 范围内

- 仓库布局与目录约定（见 [项目架构](./project-architecture.md)）
- 工具条目模板与内容规范
- 贡献流程（人工 + 可选后续脚本）
- 如何在 GitHub 上导航与审阅 PR 中的 Markdown

### 1.3 范围外（明确不做）

- **对外公开网站**、静态文档站部署（非 GitHub 仓库浏览本身）
- 完整 CMS、用户系统、评论
- 自动爬取全网工具并入库
- 替代官方文档的完整手册翻译
- 在仓库内分发大型安装包或商业授权工具破解

---

## 2. 交付形态：GitHub 仓库（非站点）

本项目的产品就是仓库本身，不是独立站点。

| 层 | 做法 | 说明 |
|----|------|------|
| 内容格式 | Markdown（+ 可选 `meta.yaml`） | 易审阅、易 PR；GitHub 原生预览 |
| 导航 | 根 README + `catalog/**/_index.md` | 无站内路由 / 无 SSG |
| 样例 | 各工具下的 `demo/`（或 `examples/`） | 克隆后本地运行或复制片段 |
| 校验 | 可选后续脚本 | 不强迫早期上 Node monorepo |
| 分享 | GitHub blob/tree 链接 | 不部署 Pages 作为主入口 |

**决策原则**：任何人只需 Git 与浏览器（打开 GitHub）即可使用目录；不必安装站点工具链。

---

## 3. 内容标准（摘要）

完整规范见 [content-standards.md](./content-standards.md)。摘要：

- 用户可见正文默认**中文**；工具专有名词、CLI 命令、配置键保持原文。
- 禁止大段粘贴受版权保护的官方手册；以摘要 + 外链为主。
- `status` 如实标注：`stub` / `draft` / `ready`（写在 README 或可选 meta）。
- 每个工具必须有 `README.md`；强烈建议有 `links.md` 与可说明的 `demo/`。
- `meta.yaml` **可选**；有则与路径一致，无则信息写在 README。
- `demo/` 必须说明如何复现；不能运行的演示需标明「示意」或「复制用片段」。

---

## 4. 工具链与环境前提

### 4.1 人人需要

- Git
- 浏览器（在 GitHub 上浏览仓库）
- 文本编辑器（建议支持 Markdown 预览）
- 阅读本仓库 `docs/` 与 `templates/tool/`

### 4.2 仅贡献内容时

- 无需安装 Node 或任何站点框架；改 Markdown（及可选 YAML）即可。
- 运行某个工具的 `demo/` 时，按其 `demo/README.md` 安装该样例自身依赖即可。

### 4.3 可选

- 后续结构校验脚本（见 `scripts/`）
- 截图工具（为 `demo/assets` 准备）

---

## 5. 如何在 GitHub 上浏览

1. 打开仓库根 [README.md](../README.md)，了解目标与结构。
2. 进入 [`catalog/_index.md`](../catalog/_index.md)，按 languages / frameworks / domains 下钻。
3. 打开某分组 `_index.md`，再进入具体工具目录阅读 `README.md`、`links.md`。
4. 需要动手时：`git clone` 本仓库，进入该工具的 `demo/`，按其说明运行或复制代码。

PR 审阅同样在 GitHub Files changed 中直接读 Markdown，无需本地起站。

---

## 6. 文件夹约定（速查）

| 路径 | 用途 |
|------|------|
| `docs/` | 架构、准备、规范、贡献——项目级文档 |
| `catalog/languages/` | 语言维度工具 |
| `catalog/frameworks/` | 框架维度工具 |
| `catalog/domains/` | 领域维度工具 |
| `templates/tool/` | 新工具复制源 |
| `scripts/` | 可选校验与脚手架（占位） |

路径段一律 kebab-case。不要在 `catalog/` 下自创第四个顶层维度，除非更新架构文档。

---

## 7. 编码 / 录内容前的短清单

在批量新增工具或完善样例前，确认：

- [ ] 已阅读 [project-architecture.md](./project-architecture.md)
- [ ] 已阅读 [content-standards.md](./content-standards.md) 与 [contributing.md](./contributing.md)
- [ ] 本地能 `git clone`，并理解用 README / `_index.md` 在 GitHub 导航
- [ ] 明确交付物是**仓库内分类 + 链接 + demo**，不是公开网站
- [ ] 至少能从 `templates/tool/` 复制出一份 **stub** 工具路径
- [ ] 若使用 `meta.yaml`，字段以「可选最小集」为准；新增字段先改规范
- [ ] `demo/` 说明了运行方式或「仅复制片段 / 仅示意」
- [ ] 中文用户文案与英文命令/配置的边界已对齐

全部勾选后再批量录入；未勾选项记为风险或单独任务。

---

## 8. 相关文档

- [项目架构](./project-architecture.md)
- [内容规范](./content-standards.md)
- [贡献指南](./contributing.md)
