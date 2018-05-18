from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'', views.home),
    url(r'^help/$', views.help),
    url(r'^about/$', views.about),
]