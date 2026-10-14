# 放入项目 urls.py 的可复制片段
from django.urls import path

from . import views  # 或 from myapp import views

urlpatterns = [
    path("hello/", views.hello),
]
