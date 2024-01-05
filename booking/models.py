from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

# Booking model


class UserDetails(models.Model):
    name = models.CharField(max_length=80, help_text='Please enter your full name')
    email = models.EmailField(help_text='Please provide a valid email address in case we need to contact you')
    guests = models.IntegerField(default=0, help_text='Please enter the number of guests in your party')
    date = models.CharField(max_length=10, help_text='Please select a date using d-m-y')
    time = models.CharField(max_length=5, help_text="Please select a time")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"{self.date} | {self.time} | {self.guests} guests | name = {self.name} | contact = {self.email}"
