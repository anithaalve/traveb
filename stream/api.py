from rest_framework.generics import ListAPIView, CreateAPIView

from .serializers import triplistserializer, trippostserializer
from .models import trips

class listtrips(ListAPIView):
  queryset = trips.objects.all()
  serializer_class = triplistserializer

class trippost(CreateAPIView):
  serializer_class = trippostserializer
