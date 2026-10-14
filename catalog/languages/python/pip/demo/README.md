# pip 演示

**可复制**片段；需本机已安装 Python 3.10+。

## 创建虚拟环境并安装

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install requests
```

## requirements.txt 示例

将同目录 [`requirements.txt`](./requirements.txt) 复制到项目根后：

```bash
python -m pip install -r requirements.txt
python -m pip freeze > requirements.lock.txt   # 可选：导出当前环境
```

## 预期结果

- `pip show requests` 能显示已安装包信息。
- 卸载：`python -m pip uninstall requests`。
