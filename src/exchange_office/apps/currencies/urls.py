from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CurrencyView

router = DefaultRouter()
router.register('', CurrencyView)

urlpatterns = router.urls