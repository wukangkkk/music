#coding=utf-8
from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'song_id_(\d+)',views.playView,name='play'),
    url(r'download_(\d+)',views.downloadView,name='download'),
]

