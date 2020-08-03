from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import CoefficientViewSet, CommerceValueViewSet
from .models import Coefficient

router = DefaultRouter()
router.register('coefficients', CoefficientViewSet, basename = Coefficient)

urlpatterns = [
    url('commerce-value/', CommerceValueViewSet.as_view({'get': 'list'})),
]

urlpatterns += router.urls