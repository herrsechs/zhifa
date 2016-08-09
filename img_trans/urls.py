from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload_hair_img/.*$', views.upload_hair_img, name='upload_hair_img'),
    url(r'^upload_head_img/.*$', views.upload_head_img, name='upload_head_img'),
    url(r'^upload_selfie_img/.*$', views.upload_selfie_img, name='upload_selfie_img'),
    url(r'^get_hair_img/.*$', views.get_hair_img, name='get_hair_img')
]