from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_trend_items/.*$', views.get_trend_items, name='get_trend_items'),
    url(r'^get_barber_haircut_gallery/.*$', views.get_barber_haircut_gallery, name='get_barber_haircut_gallery')
]
