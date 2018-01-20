from django.conf.urls import url

from . import api

urlpatterns = [
    url(r'^save/(\w+)', api.save),
    url(r'^flights/(\d+)?', api.flight),
    url(r'^airports', api.airport),
    url(r'^planes', api.plane),
]
