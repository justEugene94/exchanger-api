from django.urls import path

from . import api_views

urlpatterns = [
    path('', api_views.index, name='exchanger.index'),
]