# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.template.loader import get_template
from django.http import HttpResponse
from .models import Post
from datetime import datetime
# Create your views here.
def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
#     post_lists = list()
#     for count, post in enumerate(posts):
#         post_lists.append("No.{}:".format(str(count))+str(post)+"<br>")
    return HttpResponse(html)