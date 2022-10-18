
from .models import Property
from rest_framework import (
    viewsets,
    generics
)
from rest_framework import permissions
from api.properties.serializers import PropertySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    # permission_classes = [permissions.IsAuthenticated]

    # @staticmethod
    # def