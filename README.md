# Development Tools — GitHub 开源工具目录

本仓库是一份托管在 **GitHub 的开源开发工具目录**：按编程语言、常见框架与应用领域分类；每个工具提供外链与仓库内实现样例（可运行或可复制粘贴）。

**没有独立对外网站。** 请直接在 GitHub 上通过本 README 与 [`catalog/`](catalog/) 下的 `_index.md` 浏览；需要动手时 `git clone` 后进入对应工具的 `demo/`。

当前处于**基础脚手架**阶段：架构与规范已按「仅 GitHub 目录」对齐，工具正文以占位为主。

---

## 仓库结构（鸟瞰）

```text
docs/           项目文档（架构、开发前准备、内容规范、贡献指南）
catalog/        工具内容树：languages / frameworks / domains
templates/tool/ 新增工具时的复制模板（README + links + demo；meta.yaml 可选）
scripts/        可选校验与脚手架脚本占位
```

详细设计见 [`docs/project-architecture.md`](docs/project-architecture.md)。

---

## 如何在 GitHub 上浏览

1. 打开 [`catalog/_index.md`](catalog/_index.md) 选择维度（语言 / 框架 / 领域）。
2. 进入分组 `_index.md`，再打开具体工具目录的 `README.md`、`links.md`。
3. 克隆仓库后，按该工具 `demo/README.md` 运行或复制样例。

---

## 新人从哪读起

| 文档 | 说明 |
|------|------|
| [docs/project-architecture.md](docs/project-architecture.md) | 仓库布局、分类法、单工具包、样例共存方式 |
| [docs/pre-dev-prep.md](docs/pre-dev-prep.md) | 目标范围、克隆与 GitHub 浏览、内容清单 |
| [docs/content-standards.md](docs/content-standards.md) | 写作与可选元数据规范 |
| [docs/contributing.md](docs/contributing.md) | 如何贡献一个工具条目 |

---

## 如何贡献一个工具条目

1. 复制模板到目标路径，例如：

   ```bash
   cp -R templates/tool catalog/languages/python/poetry
   ```

2. 填写 `README.md`、`links.md`，再按需补 `demo/`（及可选的 `analysis.md` / `usage.md` / `meta.yaml`）。
3. 遵循 [内容规范](docs/content-standards.md)，提交 PR。

完整步骤见 [贡献指南](docs/contributing.md)。

---

## 分类速览

- **languages/** — 语言生态工具（包管理、测试、格式化等）
- **frameworks/** — 框架绑定工具链与脚手架
- **domains/** — 跨语言场景（web、devops、data、ai-ml 等）

---

## 许可证与贡献

欢迎通过 Issue / PR 补充 stub 或完善 draft。重大分类调整请先讨论架构文档变更。本仓库定位为开源目录，而非站点产品。
