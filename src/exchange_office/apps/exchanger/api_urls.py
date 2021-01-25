from django.urls import path

from apps.exchanger import api_views

urlpatterns = [
    path('', api_views.index, name='exchanger.index'),
]