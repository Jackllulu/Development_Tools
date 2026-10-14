# Django 演示

**可运行**（建议 Python 3.10+）：

```bash
pip install "django>=5.0,<6"
django-admin startproject mysite
cd mysite
python manage.py migrate
python manage.py runserver
```

浏览器打开 http://127.0.0.1:8000/ 。

同目录 [`views.snippet.py`](./views.snippet.py) 为可复制到 `views.py` 的最小视图；[`urls.snippet.py`](./urls.snippet.py) 展示路由挂载方式。
