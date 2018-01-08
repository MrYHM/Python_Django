# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

class BlogsPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

class Test1(models.Model):
    address = models.CharField(max_length=100)
    content = models.CharField(max_length=150)
    # def __unicode__(self):
    #     return u'%s %s'%(address,content)

admin.site.register(BlogsPost,BlogPostAdmin)
