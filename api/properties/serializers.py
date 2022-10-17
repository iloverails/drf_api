from .models import Property
from rest_framework import serializers


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
        # fields = ['title', 'description', 'price', 'rating', 'landlord']
