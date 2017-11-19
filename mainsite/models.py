# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#Create your models here.
 
from django.utils import timezone

#这是链接数据库的，数据库的表每修改后都要 python manage.py makemigrations 和python manage.py  migrate
class Dreamreal(models.Model):

   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   name = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()

   class Meta:
      db_table = "dreamreal"
  
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
     
    class Meta:
        ordering = ('-pub_date',)
         
        def __unicode__(self):
            return self.title
         
