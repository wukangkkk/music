#coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^song_id_(\d+)',views.commentView,name='comment'),
]
