from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^follow/.*$', views.follow, name='follow')
]