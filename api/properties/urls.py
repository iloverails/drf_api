from django.contrib import admin
from django.urls import include, path
from api.properties.views import PropertyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PropertyViewSet)
urlpatterns = router.urls

# urlpatterns = [
#     path('', PropertyViewSet, name='properties'),
# ]
