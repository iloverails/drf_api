from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.properties.views import PropertyViewSet

router = routers.DefaultRouter()
router.register(r'properties', PropertyViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
