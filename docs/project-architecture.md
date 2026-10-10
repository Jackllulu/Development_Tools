# 项目架构：开发工具目录（Development Tools Catalog）

本文描述本仓库的整体架构：目录布局、内容分类、单工具包形态、贡献/扩展模型，以及文档与演示如何共存。

> 权威副本位于仓库 `docs/`。Context 存档同步至 Agent Store 的 `docs/project-architecture.md`。

---

## 1. 目标一句话

建立一个**按技术栈与领域组织的开发工具目录**：每个工具条目包含分析、演示、用法与外链，后续可挂载站点浏览与检索。

---

## 2. 仓库布局

```text
/
├── README.md                 # 新人入口：目的、结构、如何贡献
├── docs/                     # 项目级文档（架构、准备、规范）
│   ├── project-architecture.md
│   ├── pre-dev-prep.md
│   ├── content-standards.md
│   └── contributing.md
├── catalog/                  # 工具内容主树（Markdown + 元数据）
│   ├── _index.md             # 目录总览与导航说明
│   ├── languages/            # 编程语言维度
│   ├── frameworks/           # 常见框架维度
│   └── domains/              # 应用领域维度
├── site/                     # 目录站点骨架（后续实现；当前仅占位）
│   └── README.md
├── scripts/                  # 校验、脚手架生成等辅助脚本（后续）
│   └── README.md
└── templates/                # 新增工具条目的模板包
    └── tool/
        ├── meta.yaml
        ├── README.md
        ├── analysis.md
        ├── usage.md
        ├── links.md
        └── demo/
            └── README.md
```

### 设计原则

| 原则 | 说明 |
|------|------|
| 内容优先 | `catalog/` 是真理来源；站点只消费内容，不内嵌业务文案 |
| 文档与演示同包 | 每个工具一个目录，分析/用法/演示/链接同级共存 |
| 薄站点 | `site/` 初期可为空壳；选型见 `pre-dev-prep.md` |
| 可脚本校验 | 元数据与文件夹约定稳定后，用脚本做结构校验 |

---

## 3. 内容分类（Taxonomy）

工具按**三个正交维度**归档。同一工具可在多个维度下出现（推荐：主归类一份实体，其余用短索引或符号链接说明；首期采用「主路径 + 交叉引用」）。

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
- 展示名写在 `meta.yaml` 的 `name` / `name_zh` 字段，不依赖文件夹大小写。

### 3.5 交叉引用

在 `meta.yaml` 中声明：

```yaml
primary: languages/python/poetry   # 实体主路径（相对 catalog/）
also_under:
  - domains/devops                 # 可选：额外出现在哪些维度下的索引
tags: [packaging, python]
```

首期可仅维护 `primary`；站点实现后再生成交叉索引页。

---

## 4. 单工具包形态（Per-tool package）

每个工具目录是一个**自洽内容包**：

```text
catalog/<dimension>/<group>/<tool-slug>/
├── meta.yaml          # 机器可读元数据（必填）
├── README.md          # 一页摘要：是什么、何时用、快速链接（必填）
├── analysis.md        # 分析：定位、优缺点、对比、适用边界（可先占位）
├── usage.md           # 用法 / How-to：安装、常用命令、典型流程（可先占位）
├── links.md           # 官方文档、仓库、生态链接（可先占位）
└── demo/              # 演示材料
    ├── README.md      # 演示说明与如何运行
    └── …              # 可选：脚本、截图、最小示例项目
```

### 4.1 `meta.yaml` 最小字段

```yaml
id: poetry                          # 全局唯一 slug，建议与目录名一致
name: Poetry
name_zh: Poetry
summary: Python 依赖与打包工具
summary_zh: Python 依赖管理与打包工具
status: stub                        # stub | draft | ready
dimension: languages                # languages | frameworks | domains
group: python                       # 语言/框架/领域 slug
tags: [python, packaging]
license_note: ""                    # 可选：许可提示
official_url: https://python-poetry.org/
repo_url: https://github.com/python-poetry/poetry
updated: 2026-10-10
```

### 4.2 四个内容面

| 文件 | 用途 | 后续形态 |
|------|------|----------|
| `analysis.md` | 分析文档：问题域、能力边界、与同类对比 | 可含表格、引用 |
| `usage.md` | How-to：安装、配置、日常命令、排错入口 | 可分小节，避免整本手册复制 |
| `demo/` | 可运行或可跟做的最小演示 | 脚本、录屏、截图；保持最小可复现 |
| `links.md` | 外链清单 | 官方、教程、相关 RFC、替代品 |

### 4.3 状态机

- `stub`：仅有目录 + `meta.yaml` + README 摘要骨架
- `draft`：四类内容至少各有初稿
- `ready`：通过内容规范自检，可进站点首页推荐

---

## 5. 文档与演示如何共存

```text
        ┌─────────────────────────────────────┐
        │  catalog/<…>/<tool>/                │
        │  meta + README + analysis + usage   │
        │              + links + demo/        │
        └─────────────────┬───────────────────┘
                          │ 构建 / 读取
                          ▼
        ┌─────────────────────────────────────┐
        │  site/  （静态站或 SSG）              │
        │  - 列表 / 检索 / 标签                 │
        │  - 渲染 Markdown                      │
        │  - 嵌入或链接 demo 说明与产物         │
        └─────────────────────────────────────┘
```

- **同目录原则**：演示不单独散落在 `site/` 或仓库根；以免内容与工具脱节。
- **演示边界**：`demo/` 内只放该工具相关的最小示例；跨工具对比放在 `docs/` 或专题页。
- **大文件**：截图/短视频可放 `demo/assets/`；超大二进制不进 Git，改用外链并在 `links.md` / `demo/README.md` 注明。
- **站点职责**：导航、搜索、主题样式；不复制粘贴工具正文。

---

## 6. 贡献与扩展模型

### 6.1 新增一个工具

1. 在 `templates/tool/` 复制到目标路径，或后续使用脚手架脚本。
2. 填写 `meta.yaml` 与 `README.md` 摘要。
3. 按优先级补齐 `analysis.md` → `usage.md` → `links.md` → `demo/`。
4. 更新所属维度的 `_index.md`（若存在）或总览。
5. 提交 PR；标题建议：`catalog: add <tool> under <dimension>/<group>`。

详见 `docs/contributing.md`。

### 6.2 新增维度分组（新语言 / 新框架 / 新领域）

1. 在对应维度下新建 `<group>/`，附 `_index.md` 说明收录范围。
2. 在 `catalog/_index.md` 登记该分组。
3. 不改动 taxonomy 三维名称，除非架构评审同意。

### 6.3 扩展站点能力

- 仅在 `site/` 与可选 `scripts/` 中演进。
- 内容 schema（`meta.yaml`）变更需同步更新：`content-standards.md`、模板、校验脚本。

### 6.4 非目标（首期）

- 不实现完整用户账号、评论系统。
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

1. **Foundation（本阶段）**：架构文档、准备文档、空目录脚手架、模板。
2. **Content seed**：若干 `stub`/`draft` 工具条目验证路径与规范。
3. **Site MVP**：列表 + 详情页渲染 Markdown。
4. **Automation**：脚手架 CLI、meta 校验、死链检查。

---

## 9. 相关文档

- [开发前准备](./pre-dev-prep.md)
- [内容规范](./content-standards.md)
- [贡献指南](./contributing.md)
