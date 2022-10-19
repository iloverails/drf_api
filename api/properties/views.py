from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.parsers import MultiPartParser

from .models import Property, PropertyImage
from rest_framework import (
    views,
    viewsets,
    generics,
    response,
    status
)
from .permissions import PropertyPermission
from api.properties.serializers import PropertySerializer, PropertyImageSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    permission_classes = (PropertyPermission, )
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    parser_classes = [MultiPartParser]
    serializer_action_classes = {
        'upload_image': PropertyImageSerializer
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    @action(detail=True, methods=['post'])
    def upload_image(self, request, pk=None):
        try:
            image = request.FILES.get('image')
            PropertyImage.objects.create(image=image, property=Property(id=pk))
        except KeyError:
            raise ParseError('Request has no resource image attached')

        return response.Response(status=status.HTTP_200_OK)

