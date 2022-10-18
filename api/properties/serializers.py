from django.utils import timezone

from .models import Property
from rest_framework import serializers
from ..users.models import User


class PropertyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'role',
        ]


class PropertySerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    rating = serializers.IntegerField()
    price = serializers.FloatField()
    landlord = PropertyUserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = Property
        fields = [
            'title',
            'description',
            'rating',
            'price',
            'landlord'
        ]
