from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout

from rest_framework.urlpatterns import format_suffix_patterns
from registry import views as registryviews
from stream import views as streamviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login, {'template_name': 'registry/login.html'}),
    url(r'^logout/', logout, {'template_name': 'registry/logout.html'}),
    url(r'^signup/', registryviews.signupformview.as_view(), name='signup'),
    url(r'^profile/', registryviews.profile, name = 'profile'),

    url(r'^api/', include('api.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^$', TemplateView.as_view(template_name='stream/stream.html'), name = 'stream'),
]
