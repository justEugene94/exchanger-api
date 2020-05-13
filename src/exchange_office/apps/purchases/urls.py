from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views

# router = DefaultRouter()
# router.register('',  PurchaseView.as_view())

urlpatterns = [
    path('', views.get, name='purchase.get'),
    path('create/', views.post, name='purchase.post'),
    path('<int:pk>', views.show, name='purchase.show'),
]