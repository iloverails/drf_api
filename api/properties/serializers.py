from .models import Property
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'title',
            'description',
            'rating',
            'price',
            'landlord'
        ]
