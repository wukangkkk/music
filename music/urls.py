#coding=utf-8
"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import url
from django.views import static
from django.conf import settings

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', include('index.urls')),
    url('^ranking.html$', include('ranking.urls')),
    url('play/', include('play.urls')),
    url('comment/', include('comment.urls')),
    url('search/', include('search.urls')),
    url('user/', include('user.urls')),
    # 设置项目上线的静态资源路径
    url('^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static')
]


# 设置404、500错误状态码
from index import views
handler404 = views.page_not_found
handler500 = views.page_not_found