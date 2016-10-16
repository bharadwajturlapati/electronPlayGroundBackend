__author__ = 'bharadwaj'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^snippets/$', views.call_delegate)
]