from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^follow/.*$', views.follow, name='follow'),
    url(r'^followList/.*$', views.follow_list, name='follow_list'),
    url(r'^comment/.*$', views.comment, name='comment'),
    url(r'^get_img_comment/.*$', views.get_img_comment, name='get_img_comment'),
    url(r'^favor_img/.*$', views.favor_img, name='favor_img'),
    url(r'^upload_barber_message/.*$', views.upload_barber_message, name='upload_barber_message'),
    url(r'^get_customer_message/.*$', views.get_customer_message, name='get_customer_message')
]