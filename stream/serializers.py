from rest_framework import serializers
from .models import trips

class triplistserializer(serializers.ModelSerializer):
  class Meta:
    model= trips

    #return only selected column
    #fields = ('gid', 'fromlocation', 'tolocation', 'leavingon', 'reachingon', 'angel')

    #return all cloumn data
    fields = '__all__'

class trippostserializer(serializers.ModelSerializer):
  class Meta:
    model= trips
    fields = '__all__'
