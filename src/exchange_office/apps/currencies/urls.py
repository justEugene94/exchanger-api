from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CurrencyView
from .models import Currency

router = DefaultRouter()
router.register('currencies', CurrencyView, basename = Currency)

urlpatterns = router.urls