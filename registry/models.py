# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userprofile(models.Model):
  username = models.OneToOneField(User)
  email = models.CharField(max_length=30)
  city = models.CharField(max_length=100,default='')
  gender = models.CharField(max_length=10, default='')
  phonenumber = models.IntegerField(default=0)
