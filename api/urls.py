from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from registry import views as registryviews
from stream import views as streamviews
from stream import api as baseapis

urlpatterns = [
    url(r'^listtrips$', baseapis.listtrips.as_view(), name = 'LISTTRIPS'),
    url(r'^trippost$', streamviews.trippost.as_view(), name = 'TRIPPOST'),
]
