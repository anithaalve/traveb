# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import json, datetime, time, calendar
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import trips
from .serializers import triplistserializer

#
#List all trips or create one
#url '/'
#
class listtrips(APIView):

  def get(self, request):
    # Force user to login to see trip list
    #if request.user.is_authenticated():
      triplist = trips.objects.all()
      serializer = triplistserializer(triplist, many=True)
      templatename = 'stream/stream.html'
      return render(request, templatename, {'triplist': serializer.data})
    #else:
      #return Redirect('/login')

class trippost(APIView):

  def post(self, request):
    import datetime
    tripdata = json.loads(request.body)['tripdata']
    now = int(datetime.datetime.now().strftime("%s"))
    queryset = trips.objects.create(createdon= now, modifiedon= now, fromlocation= tripdata['fromlocation'], tolocation= tripdata['tolocation'], leavingon= tripdata['leavingon'], reachingon= tripdata['reachingon'], angel='Saikat', timezoneoffset=tripdata['timezoneoffset'])
    time.sleep(5)
    return HttpResponse(queryset)

