# 开发前准备（Pre-development Preparation）

在批量录入工具内容或补充演示样例之前，先对齐目标、内容规范与本地环境。读完本文并勾选文末清单后再开工。

> **形态澄清**：本项目是 **GitHub 开源目录**（Markdown + `meta.yaml` + `demo/`），不是网站产品。不要引入 Astro、VitePress 或其他站点工程作为交付目标。

---

## 1. 目标与范围

### 1.1 目标

- 沉淀一份**结构化、可扩展**的开发工具目录（语言 / 框架 / 领域）。
- 每个工具具备统一四件套：**分析、用法、演示（实现样例）、链接**。
- 在 GitHub 上通过文件树与 Markdown 导航阅读；用 PR 协作维护。

### 1.2 范围内

- 仓库布局与目录约定（见 [项目架构](./project-architecture.md)）
- 工具条目模板与内容规范
- 贡献流程（人工 + 可选校验脚本）
- 分类索引（`catalog/**/_index.md`）与示例演示

### 1.3 范围外（明确不做）

- **独立开放网站 / 文档站**（无 `site/` 产品、无 SSG/文档站框架选型与实现）
- 完整 CMS、用户系统、评论
- 自动爬取全网工具并入库
- 替代官方文档的完整手册翻译
- 在仓库内分发大型安装包或商业授权工具破解

---

## 2. 技术选型（目录仓库）

以**内容仓库**为唯一产品面；工具链保持轻量：

| 层 | 推荐 | 理由 |
|----|------|------|
| 内容格式 | Markdown + `meta.yaml` | 易审阅、易 PR、GitHub 原生预览 |
| 导航 | `README.md` + `catalog/**/_index.md` | 无需构建即可浏览分类 |
| 演示 | 各工具包内 `demo/` | 实现样例与说明同目录共存 |
| 校验 | 可选后续脚本读 `meta.yaml` | 不强迫早期上重型工具链 |
| 协作 | GitHub Issues / PR | 与开源目录形态一致 |

**决策原则**：任何自动化都必须服务 `catalog/` 内容；不引入站点工程阻塞贡献。

---

## 3. 内容标准（摘要）

完整规范见 [content-standards.md](./content-standards.md)。摘要：

- 用户可见正文默认**中文**；工具专有名词、CLI 命令、配置键保持原文。
- 禁止大段粘贴受版权保护的官方手册；以摘要 + 外链为主。
- `status` 如实标注：`stub` / `draft` / `ready`。
- 每个工具必须有 `meta.yaml` 与 `README.md`。
- `demo/` 必须说明如何复现；不能运行的演示需标明「示意」。

---

## 4. 工具链与环境前提

### 4.1 人人需要

- Git
- 文本编辑器（建议支持 Markdown 预览）
- 阅读本仓库 `docs/` 与 `templates/tool/`

### 4.2 仅贡献内容时

- 无需安装 Node 或其他运行时；改 Markdown / YAML 即可。
- 在 GitHub 网页或本地预览 Markdown。

### 4.3 补充可运行演示时

- 按该工具 `demo/README.md` 安装其自身依赖（语言/包管理器因工具而异）。
- 不在仓库根强制统一前端站点依赖。

### 4.4 可选

- `yamllint` / Schema 校验（待脚本落地后）
- 截图工具（为 `demo/assets` 准备）

---

## 5. 文件夹约定（速查）

| 路径 | 用途 |
|------|------|
| `docs/` | 架构、准备、规范、贡献——项目级文档 |
| `catalog/languages/` | 语言维度工具 |
| `catalog/frameworks/` | 框架维度工具 |
| `catalog/domains/` | 领域维度工具 |
| `templates/tool/` | 新工具复制源 |
| `scripts/` | 可选校验与脚手架（占位） |

**不设 `site/`**。路径段一律 kebab-case。不要在 `catalog/` 下自创第四个顶层维度，除非更新架构文档。

---

## 6. 开工前短清单

在批量录入或完善演示前，确认：

- [ ] 已阅读 [project-architecture.md](./project-architecture.md)
- [ ] 已阅读 [content-standards.md](./content-standards.md) 与 [contributing.md](./contributing.md)
- [ ] 本地能 `git clone` / 拉取本分支，且理解交付物是 `catalog/` + `demo/`，不是网站
- [ ] 至少有一份从 `templates/tool/` 复制出的 **stub** 工具路径可用来验证约定
- [ ] `meta.yaml` 字段集合已冻结到「最小可用」；新增字段先改规范再改脚本
- [ ] 明确首期交付：纯内容 / stub 条目 **或** 带可运行 demo 的 draft（写进任务描述）
- [ ] 中文用户文案与英文-only 文件（如部分配置）的边界已对齐

全部勾选后再进入批量内容工作；未勾选项记为风险或单独任务。

---

## 7. 相关文档

- [项目架构](./project-architecture.md)
- [内容规范](./content-standards.md)
- [贡献指南](./contributing.md)
