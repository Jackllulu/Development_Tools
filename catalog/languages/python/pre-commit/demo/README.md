# pre-commit 演示

**可复制**配置；需已是 Git 仓库且可安装 Python 包。

```bash
pip install pre-commit
# 将 .pre-commit-config.yaml 放到仓库根
pre-commit install
pre-commit run --all-files
```

配置见 [`.pre-commit-config.yaml`](./.pre-commit-config.yaml)（含 `pre-commit-hooks` 与 Ruff 示例）。
