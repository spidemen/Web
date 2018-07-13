# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=15)
    dept= models.CharField(max_length=30)
    class Meta:
        db_table = 'user'

class blog(models.Model):
    content = models.CharField(max_length=255,primary_key=True)
    class Meta:
        db_table = 'blog'