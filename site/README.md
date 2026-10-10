# site/

目录浏览站点的占位目录。

- **现状**：无应用代码；内容源在仓库根下的 `catalog/`。
- **计划**：采用静态站点生成（选型见 `docs/pre-dev-prep.md`，默认倾向 Astro 或 VitePress），读取 `catalog/**/meta.yaml` 与 Markdown 渲染列表与详情页。
- **约束**：不在此目录复制工具正文；演示与文档留在各工具包内。

实现 MVP 前请先勾选 `docs/pre-dev-prep.md` 文末清单。
