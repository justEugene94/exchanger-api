from django.urls import path, include

urlpatterns = [
    path('', include('exchanger.urls')),
    path('', include('currencies.urls')),
    path('', include('coefficients.urls')),
    path('', include('purchases.urls')),
]

