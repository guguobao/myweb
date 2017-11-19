"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#!/usr/bin/python
# -*- coding: <utf-8> -*-
from django.conf.urls import include,url,patterns
from django.contrib import admin
#from django.conf import settings
from mainsite.views import viewArticle,crudops,Redirect,viewArticleother,ViewArticles
from mainsite.views import homepage ,sendSimpleEmail
import re

urlpatterns = [
    url(r'^view',homepage),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/(\d+)/', viewArticle, name ='article'),
    url(r'^articleother/(\d+)/', viewArticleother, name ='article2'),
    url(r'^crudops', crudops, name='crudops'),
    url(r'^redirect',Redirect, name='Redirect'),
    url(r'^articles/(\d{2})/(\d{4})/',ViewArticles,name='articles'),
    url(r'^simpleemail/(?P<emailto> [\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/', 'sendSimpleEmail' , name = 'sendSimpleEmail'),
]


