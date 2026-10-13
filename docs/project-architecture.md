# 项目架构：开发工具目录（Development Tools Catalog）

本文描述本仓库的整体架构：目录布局、内容分类、单工具包形态、贡献/扩展模型，以及文档与实现样例如何共存。

> 权威副本位于仓库 `docs/`。Context 存档同步至 Agent Store 的 `docs/project-architecture.md`。

---

## 1. 目标一句话

建立一个 **GitHub 开源工具目录**：按技术栈与领域组织分类；每个工具条目包含外链与仓库内可运行/可复制的实现样例。浏览与导航只依赖 GitHub 上的 `README.md` 与各级 `_index.md`，**不提供独立对外网站**。

---

## 2. 仓库布局

```text
/
├── README.md                 # 新人入口：目的、结构、如何在 GitHub 浏览与贡献
├── docs/                     # 项目级文档（架构、准备、规范）
│   ├── project-architecture.md
│   ├── pre-dev-prep.md
│   ├── content-standards.md
│   └── contributing.md
├── catalog/                  # 工具内容主树（Markdown；可选 YAML）
│   ├── _index.md             # 目录总览与导航
│   ├── languages/            # 编程语言维度
│   ├── frameworks/           # 常见框架维度
│   └── domains/              # 应用领域维度
├── scripts/                  # 可选：校验、脚手架等辅助脚本（后续）
│   └── README.md
└── templates/                # 新增工具条目的模板包
    └── tool/
        ├── README.md         # 摘要（必填）
        ├── links.md          # 外链（必填倾向）
        ├── analysis.md       # 分析（可选）
        ├── usage.md          # 用法（可选）
        ├── meta.yaml         # 可选结构化字段（便于脚本；GitHub 浏览不依赖）
        └── demo/             # 实现样例（可运行或可复制粘贴）
            └── README.md
```

### 设计原则

| 原则 | 说明 |
|------|------|
| GitHub 即产品 | 分类、链接、样例全部在仓库内；用 GitHub 文件树与 Markdown 预览浏览 |
| 内容优先 | `catalog/` 是真理来源；无站点生成器、无独立 `site/` 交付物 |
| 文档与样例同包 | 每个工具一个目录，链接与 `demo/`（或 `examples/`）同级共存 |
| 导航极简 | 仅靠根 `README.md` + 各层 `_index.md`；不另建站内路由 |
| 元数据可选 | `README.md` 足够人类浏览；`meta.yaml` 仅在需要脚本/批量校验时使用 |

---

## 3. 内容分类（Taxonomy）

工具按**三个正交维度**归档。同一工具可在多个维度下出现（推荐：主归类一份实体，其余用交叉引用；首期采用「主路径 + README 交叉引用」）。

### 3.1 `languages/` — 编程语言

- 按语言 slug 分文件夹，例如 `python/`、`typescript/`、`go/`、`rust/`。
- 其下再按工具 slug，例如 `catalog/languages/python/poetry/`。
- 收录语言本身相关的包管理、调试、格式化、测试、构建等工具。

### 3.2 `frameworks/` — 常见框架

- 按框架生态 slug，例如 `react/`、`django/`、`spring/`、`nextjs/`。
- 收录框架官方工具链、脚手架、插件与强绑定周边工具。

### 3.3 `domains/` — 应用领域

- 按领域 slug，例如 `web/`、`mobile/`、`data/`、`devops/`、`security/`、`ai-ml/`。
- 收录跨语言、按场景选型的工具（CI、容器、可观测性、API 设计等）。

### 3.4 命名约定

- 所有路径段使用 **kebab-case** 小写 ASCII（`ai-ml`、`nextjs`）。
- 展示名写在 `README.md` 标题（及可选的 `meta.yaml` 的 `name` / `name_zh`），不依赖文件夹大小写。

### 3.5 交叉引用

在工具 `README.md` 中注明主路径与其他相关维度；若使用可选 `meta.yaml`，可声明：

```yaml
primary: languages/python/poetry   # 实体主路径（相对 catalog/）
also_under:
  - domains/devops
tags: [packaging, python]
```

首期可仅在 README 写交叉引用；后续如有脚本再生成索引列表。

---

## 4. 单工具包形态（Per-tool package）

每个工具目录是一个**自洽内容包**：

```text
catalog/<dimension>/<group>/<tool-slug>/
├── README.md          # 一页摘要：是什么、何时用、快速链接（必填）
├── links.md           # 官方文档、仓库、生态链接（强烈建议）
├── analysis.md        # 分析：定位、优缺点、对比（可选）
├── usage.md           # 用法 / How-to（可选；短步骤可直接写在 README）
├── meta.yaml          # 可选：机器可读字段
└── demo/              # 实现样例（推荐；亦可命名 examples/）
    ├── README.md      # 如何运行或如何复制粘贴
    └── …              # 脚本、最小示例、片段文件
```

> `demo/` 与 `examples/` 二选一即可；模板默认使用 `demo/`。较大可独立运行的样例项目放在该目录下，保持与工具条目同包。

### 4.1 可选 `meta.yaml`（非站点生成专用）

GitHub 浏览**不依赖** YAML。若团队希望统一字段或跑校验脚本，可使用最小集合：

```yaml
id: poetry
name: Poetry
name_zh: Poetry
summary_zh: Python 依赖管理与打包工具
status: stub                        # stub | draft | ready
dimension: languages
group: python
tags: [python, packaging]
official_url: https://python-poetry.org/
repo_url: https://github.com/python-poetry/poetry
updated: 2026-10-13
```

无 `meta.yaml` 时，以上信息应出现在 `README.md` 中。

### 4.2 内容面

| 文件 / 目录 | 用途 |
|-------------|------|
| `README.md` | 摘要、适用场景、指向本包其余文件与外链 |
| `links.md` | 外链清单：官方、仓库、教程、替代品 |
| `demo/` 或 `examples/` | 可运行或可复制粘贴的最小实现样例 |
| `analysis.md` / `usage.md` | 可选：更深分析与 How-to |

### 4.3 状态（写在 README 或可选 meta）

- `stub`：目录 + README 骨架（可仅有链接占位）
- `draft`：链接齐全，样例或用法至少有初稿
- `ready`：规范自检通过，样例可复现或已标明「仅示意」

---

## 5. 文档与实现样例如何共存

```text
        ┌─────────────────────────────────────┐
        │  catalog/<…>/<tool>/                │
        │  README + links +（可选）analysis   │
        │              + demo/ 或 examples/   │
        └─────────────────┬───────────────────┘
                          │  GitHub 浏览
                          ▼
        ┌─────────────────────────────────────┐
        │  README.md / 各级 _index.md         │
        │  - 分类导航                           │
        │  - 点进工具目录读 Markdown             │
        │  - 克隆后本地运行 demo                 │
        └─────────────────────────────────────┘
```

- **同目录原则**：样例不散落在仓库根或虚构的站点目录；以免与工具脱节。
- **样例边界**：`demo/` 内只放该工具相关的最小示例；跨工具对比放在 `docs/`。
- **大文件**：截图/短视频可放 `demo/assets/`；超大二进制不进 Git，改用外链并在 `links.md` / `demo/README.md` 注明。
- **无独立站点**：不部署 Pages/文档站作为主交付；需要分享时直接给 GitHub 路径或 raw/blob 链接。

---

## 6. 贡献与扩展模型

### 6.1 新增一个工具

1. 复制 `templates/tool/` 到目标路径。
2. 填写 `README.md` 与 `links.md`；按需补 `demo/` 与可选文件。
3. 更新所属分组与维度的 `_index.md`（若列出具体工具）。
4. 提交 PR；标题建议：`catalog: add <tool> under <dimension>/<group>`。

详见 `docs/contributing.md`。

### 6.2 新增维度分组（新语言 / 新框架 / 新领域）

1. 在对应维度下新建 `<group>/`，附 `_index.md` 说明收录范围。
2. 在 `catalog/_index.md` 登记该分组。
3. 不改动 taxonomy 三维名称，除非架构评审同意。

### 6.3 可选自动化

- 仅在 `scripts/` 中演进（结构校验、死链检查等）。
- 若调整可选 `meta.yaml` 字段，同步更新 `content-standards.md` 与模板。

### 6.4 非目标

- **不做**对外公开网站 / SSG 站点产品（Astro、VitePress、GitHub Pages 站点等均非交付目标）。
- 不实现用户账号、评论系统。
- 不托管工具二进制安装包。
- 不替代各工具官方文档全文。

---

## 7. 与 Agent Store / Context 的关系

| 位置 | 角色 |
|------|------|
| 仓库 `docs/`、`catalog/`、`README.md` | **主源**（版本控制、协作、CI） |
| `/cursor/stores/.../docs/` | 项目 Context 同步副本，便于协调与检索 |

以仓库为准；若两边短暂不一致，以 Git 提交为准并回写 Context。

---

## 8. 演进路线（架构视角）

1. **Foundation（本阶段）**：架构文档、准备文档、空目录脚手架、模板（GitHub 目录形态）。
2. **Content seed**：若干 `stub`/`draft` 工具条目（链接 + 样例）验证路径与规范。
3. **Enrich**：补齐常用工具的可复制 demo；完善 `_index.md` 导航。
4. **Automation（可选）**：脚手架 CLI、可选 meta 校验、死链检查。

---

## 9. 相关文档

- [开发前准备](./pre-dev-prep.md)
- [内容规范](./content-standards.md)
- [贡献指南](./contributing.md)
