from rest_framework.routers import DefaultRouter

from .views import CoefficientViewSet
from .models import Purchase

router = DefaultRouter()
router.register('', CoefficientViewSet, basename = Purchase)

urlpatterns = router.urls