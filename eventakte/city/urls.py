# -*- encoding: utf-8 -*-
from django.conf.urls import            url

from . import views

urlpatterns = [
    url(r'^(?P<slug>.+)$', views.change_city_1, name="select-city"),
]