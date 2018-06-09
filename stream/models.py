# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class trips(models.Model):
  #gid data convention "object_timezone_id"
  createdon      = models.CharField(max_length=16)
  modifiedon     = models.CharField(max_length=16)
  fromlocation   = models.CharField(max_length=256)
  tolocation     = models.CharField(max_length=256)
  leavingon      = models.CharField(max_length=64)
  reachingon     = models.CharField(max_length=64)
  angel          = models.CharField(max_length=64)
  timezoneoffset = models.CharField(max_length=64,default = None)

  #defining enum for status
  statusenum = ((0, 'ACTIVE'),(1, 'INACTIVE'))
  status         = models.CharField(max_length=1, choices=statusenum)

  def __str__(self):
    return str(self.id)

