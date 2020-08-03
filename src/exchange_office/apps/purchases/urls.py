from django.urls import path

from . import views


urlpatterns = [
    path('purchases/', views.get, name='purchase.get'),
    path('purchases/create/', views.post, name='purchase.post'),
    path('purchases/<int:pk>/', views.show, name='purchase.show'),
]