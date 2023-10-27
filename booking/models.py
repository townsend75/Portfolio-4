from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField


STATUS = ((0, "Unconfirmed"), (1, "Confirmed"))

TIME_CHOICES = (
    ('11:00', '11:00'),
    ('11:30', '11:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
)

# Booking model 
class UserDetails(models.Model):
    name = models.CharField(max_length=80, help_text='Please enter your full name')
    email = models.EmailField(help_text='Please provide a valid email address in case we need to contact you')
    guests = models.IntegerField(default=0, help_text='Please enter the number of guests in your party')
    date = models.CharField(max_length=10, help_text='Please select a date using d-m-y')
    time = models.CharField(max_length=5, help_text="Please select a time")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
   
    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"{self.date} | {self.time} | {self.guests} guests | name = {self.name} | contact = {self.email}"


class Reviews(models.Model):
    post = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="reviews")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
  
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Review {self.body} from {self.name}"
