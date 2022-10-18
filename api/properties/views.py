from .models import Property
from rest_framework import (
    viewsets,
    generics
)
from .permissions import PropertyPermission
from api.properties.serializers import PropertySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    permission_classes = (PropertyPermission, )
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    # @staticmethod
    # def create(self, request, *args, **kwargs):
    #     property = Property
    # def create(self, serializer):
    #     serializer.save(landlord=self.request.user)
