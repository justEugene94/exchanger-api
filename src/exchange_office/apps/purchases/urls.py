from django.urls import path

from . import views


urlpatterns = [
    path('', views.get, name='purchase.get'),
    path('create/', views.post, name='purchase.post'),
    path('<int:pk>/', views.show, name='purchase.show'),
]