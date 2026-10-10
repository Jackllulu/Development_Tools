# 开发前准备（Pre-development Preparation）

在实现站点功能或批量录入工具内容之前，先对齐目标、技术选型、内容规范与本地环境。读完本文并勾选文末清单后再开工。

---

## 1. 目标与范围

### 1.1 目标

- 沉淀一份**结构化、可扩展**的开发工具目录（语言 / 框架 / 领域）。
- 每个工具具备统一四件套：**分析、用法、演示、链接**。
- 为后续静态站点或文档站提供干净的内容源与约定。

### 1.2 范围内

- 仓库布局与目录约定（见 [项目架构](./project-architecture.md)）
- 工具条目模板与内容规范
- 站点技术选型与最小实现路径
- 贡献流程（人工 + 后续脚本）

### 1.3 范围外（首期明确不做）

- 完整 CMS、用户系统、评论
- 自动爬取全网工具并入库
- 替代官方文档的完整手册翻译
- 在仓库内分发大型安装包或商业授权工具破解

---

## 2. 站点 / 目录本身的技术选型

首期以**内容仓库**为主；站点可后置。推荐默认选型如下（可在 MVP 前再确认一次）：

| 层 | 推荐 | 理由 |
|----|------|------|
| 内容格式 | Markdown + YAML front/`meta.yaml` | 易审阅、易 PR、工具链成熟 |
| 站点框架 | Astro 或 VitePress | 静态友好、MD 一等公民、部署简单 |
| 包管理 | pnpm | 磁盘友好、锁文件清晰 |
| 语言 | TypeScript（仅 `site/`） | 与常见前端栈一致 |
| 校验 | 后续 Node 脚本读 `meta.yaml` | 不强迫早期上 monorepo 重工具 |
| 部署 | 静态托管（GitHub Pages / Cloudflare Pages 等） | 与只读目录匹配 |

**决策原则**：站点不得成为内容瓶颈；即使站点未就绪，`catalog/` 仍可独立贡献与审阅。

若团队更熟 Next.js，可用「MDX + 静态导出」替代，但需在开工前写入本节并更新架构「演进路线」。

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

- 无需安装 Node；改 Markdown / YAML 即可。

### 4.3 开发站点时（后续）

- Node.js LTS（建议 20+）
- pnpm（或团队统一的包管理器）
- 按 `site/README.md` 安装依赖并本地预览

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
| `site/` | 站点代码（占位 → MVP） |
| `scripts/` | 校验与脚手架（占位） |

路径段一律 kebab-case。不要在 `catalog/` 下自创第四个顶层维度，除非更新架构文档。

---

## 6. 编码功能前的短清单

在写站点代码或批量生成页面前，确认：

- [ ] 已阅读 [project-architecture.md](./project-architecture.md)
- [ ] 已阅读 [content-standards.md](./content-standards.md) 与 [contributing.md](./contributing.md)
- [ ] 本地能 `git clone` / 拉取本分支，且理解 `catalog/` 与 `site/` 边界
- [ ] 站点选型已在本节确认（Astro / VitePress / 其他），并记入提交说明或 issue
- [ ] 至少有一份从 `templates/tool/` 复制出的 **stub** 工具路径可用来试渲染
- [ ] `meta.yaml` 字段集合已冻结到「最小可用」；新增字段先改规范再改代码
- [ ] 明确首期交付：空壳导航 + 单工具详情 **或** 纯内容 PR（二选一写进任务描述）
- [ ] 中文用户文案与英文-only 文件（如部分配置）的边界已对齐

全部勾选后再进入功能开发；未勾选项记为风险或单独任务。

---

## 7. 相关文档

- [项目架构](./project-architecture.md)
- [内容规范](./content-standards.md)
- [贡献指南](./contributing.md)
