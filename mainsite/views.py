# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from django.template.loader import get_template
from django.http import HttpResponse
from .models import Post ,Dreamreal
from datetime import datetime
#发邮件
from django.core.mail import send_mail

def sendSimpleEmail(request,emailto):
  #发送邮件
   res = send_mail("hello paul", "comment tu vas?", "1690259624@qq.com", [emailto])
   return HttpResponse('%s'%res)


# Create your views here.
def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)

def Redirect(request):
  #用于测试重定向,用时要导包
   return redirect("https://www.djangoproject.com")
 
def viewArticleother(request, articleId):
  #重定义的另一种使用
   """ A view that display an article based on his ID"""
   text = "Displaying article Number : %s" %articleId
   return redirect(articles, year = "2045", month = "02")
	
def ViewArticles(request, year, month):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)

def crudops(request):#用于测试模块连接数据库成都情况
   #Creating an entry
    
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   
   #Read ALL entries
   objects = Dreamreal.objects.all()
   res ='Printing all Dreamreal entries in the DB : <br>'
   
   for elt in objects:
      res += elt.name+"<br>"
   
   #Read a specific entry:
   sorex = Dreamreal.objects.get(name = "sorex")
   res += 'Printing One entry <br>'
   res += sorex.name
   
   #Delete an entry
   res += '<br> Deleting an entry <br>'
   sorex.delete()
   
   #Update
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   res += 'Updating entry<br>'
   
   dreamreal = Dreamreal.objects.get(name = 'sorex')
   dreamreal.name = 'thierry'
   dreamreal.save()
   
   return HttpResponse(res)


def baidu(request,url):
  template = get_template('index.html')
  urldownload=''
  try:
    p = Baidu.objects.get(url=url)
  except Baidu.DoesNotExist:
    urldownload='没有找到下载地址'
  urldownload='www.guguobao.com'
  html = template.render({'urlbaidu':urldownload})
  return HttpResponse(html)
  
  
  