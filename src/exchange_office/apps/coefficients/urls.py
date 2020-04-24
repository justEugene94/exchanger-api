from rest_framework.routers import DefaultRouter

from .views import CoefficientViewSet
from .models import Coefficient

router = DefaultRouter()
router.register('', CoefficientViewSet, basename = Coefficient)

urlpatterns = router.urls