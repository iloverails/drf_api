from django.db import models

# Create your models here.
from django.db import models
from api.users.models import User
from django.utils import timezone


class Property(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    rating = models.IntegerField()
    price = models.FloatField()
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, related_name="landlord")
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)


class Review(models.Model):
    property = models.ForeignKey(Property, related_name='reviews', on_delete=models.CASCADE)
    description = models.TextField()
    rate = models.IntegerField()
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tenant")
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
