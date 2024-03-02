from django.urls import path, include  # Update to import the recommended functions
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns += [
    path('login/', include('django.contrib.auth.urls')),
    path('', include('sigVentas.urls')),  # Tu app
]
