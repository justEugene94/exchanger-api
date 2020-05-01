from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import PurchaseView

# router = DefaultRouter()
# router.register('',  PurchaseView.as_view())

urlpatterns = [
    path('', PurchaseView.as_view())
]