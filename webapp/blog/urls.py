# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
#传参是将请求的地址加上参数传递给views中定义的函数，进行操作，这个方式可以传递安卓手机需要传递的搜寻的参数
urlpatterns = [
    url(r'^$', views.index, name='index'),
]