from rest_framework.routers import DefaultRouter

from .views import CoefficientView
from .models import Coefficient

router = DefaultRouter()
router.register('', CoefficientView, basename = Coefficient)

urlpatterns = router.urls