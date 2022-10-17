from .models import User
from rest_framework import serializers


# Create your models here.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


