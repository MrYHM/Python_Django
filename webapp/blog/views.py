# -*- coding: utf-8 -*-
from django.shortcuts import render
from blog.models import BlogsPost
from blog.models import Test1
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404

def index(request):
    # 获取所有数据
    blog_list = BlogsPost.objects.all()
    return render_to_response('index.html',{'blog_list': blog_list})




