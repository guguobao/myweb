# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post
from .models import Dreamreal
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')

# class DreamReal(admin.ModelAdmin):
#     list_display=('website','mail','phonenumber','name')
admin.site.register(Post,PostAdmin)
admin.site.register(Dreamreal)#新建一个表，要注册，这样就能在admin后台管理