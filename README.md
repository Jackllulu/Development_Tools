# Development Tools

面向多技术栈的**开发工具目录**（GitHub 开源项目）：按编程语言、常见框架与应用领域组织条目；每个工具包含分析、用法、实现样例（`demo/`）与外链。

**本仓库不是网站产品。** 内容以 Markdown + YAML 元数据形式存在于 `catalog/`，在 GitHub 上直接浏览与贡献；不建设 Astro / VitePress 等独立站点。

当前处于**基础脚手架**阶段：架构与规范已就绪，工具正文以占位为主。

---

## 仓库结构（鸟瞰）

```text
docs/           项目文档（架构、开发前准备、内容规范、贡献指南）
catalog/        工具内容树：languages / frameworks / domains
templates/tool/ 新增工具时的复制模板（含 demo/）
scripts/        可选：校验与脚手架脚本占位
```

详细设计见 [`docs/project-architecture.md`](docs/project-architecture.md)。

---

## 新人从哪读起

| 文档 | 说明 |
|------|------|
| [docs/project-architecture.md](docs/project-architecture.md) | 仓库布局、分类法、单工具包形态、文档与演示共存方式 |
| [docs/pre-dev-prep.md](docs/pre-dev-prep.md) | 目标范围、环境前提、开工清单（无站点选型） |
| [docs/content-standards.md](docs/content-standards.md) | 写作与元数据规范 |
| [docs/contributing.md](docs/contributing.md) | 如何贡献一个工具条目 |

---

## 如何贡献一个工具条目

1. 复制模板到目标路径，例如：

   ```bash
   cp -R templates/tool catalog/languages/python/poetry
   ```

2. 填写 `meta.yaml`、`README.md`，再按需补 `analysis.md` / `usage.md` / `links.md` / `demo/`。
3. 遵循 [内容规范](docs/content-standards.md)，提交 PR。

完整步骤见 [贡献指南](docs/contributing.md)。

---

## 分类速览

- **languages/** — 语言生态工具（包管理、测试、格式化等）
- **frameworks/** — 框架绑定工具链与脚手架
- **domains/** — 跨语言场景（web、devops、data、ai-ml 等）

从 [`catalog/_index.md`](catalog/_index.md) 进入分类导航。

---

## 许可证与贡献

欢迎通过 Issue / PR 补充 stub 或完善 draft（含演示样例）。重大分类调整请先讨论架构文档变更。
