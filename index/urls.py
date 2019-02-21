#coding=utf-8
from django.conf.urls import url
from . import views

# 设置首页的URL地址信息
urlpatterns = [
    url('', views.indexView, name='index'),
]
