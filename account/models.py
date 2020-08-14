from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    DOB = models.CharField(max_length=30, null=True, blank=True)
    Location = models.CharField(max_length=100, null=True, blank=True)
    Budget = models.CharField(max_length=100, null=True,)


class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Cuisine = models.TextField(null=True, blank=True)
    Lifestyle = models.TextField(null=True, blank=True)
    Sportevent = models.TextField(null=True, blank=True)
    Travel = models.TextField(null=True, blank=True)
    Entertainment_events = models.TextField(null=True, blank=True)
    Hobbies = models.TextField(null=True, blank=True)
