from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField

# Create your models here.


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.Charfield(max_length=80)
    email = models.EmailField()
    number_of_guests = models.IntegerField
    date = models.DateField(default=datetime.now)
    time = models.TimeField(default=datetime.now)