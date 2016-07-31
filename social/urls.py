from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^follow/.*$', views.follow, name='follow'),
    url(r'^followList/.*$', views.follow_list, name='follow_list')
]