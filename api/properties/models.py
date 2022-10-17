from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from api.users.models import Landlord


class Property(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    rating = models.IntegerField()
    price = models.FloatField()
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images')


class Review(models.Model):
    property = models.ForeignKey(Property, related_name='reviews', on_delete=models.CASCADE)
    description = models.TextField()
    rate = models.IntegerField()
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)
