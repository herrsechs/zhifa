from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_trend_items/.*$', views.get_trend_items, name='get_trend_items'),
]
