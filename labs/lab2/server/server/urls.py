from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^api/', include('server.api_urls')),
    url(r'^', views.home)
]

urlpatterns += staticfiles_urlpatterns()
