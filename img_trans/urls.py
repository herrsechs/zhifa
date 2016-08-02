from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload_hair_img/.*$', views.upload_hair_img, name='upload_hair_img')
]