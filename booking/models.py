from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField


STATUS = ((0, "Unconfirmed"), (1, "Confirmed"))

TIME_CHOICES = (
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


class UserDetails(models.Model):
    name = models.CharField(max_length=80, help_text='Please enter your full name')
    email = models.EmailField(help_text='Please provide a valid email address in case we need to contact you')
    guests = models.IntegerField(default=0, help_text='Please enter the number of guests in your party')
    date = models.DateField(default=datetime.now, help_text='Please select a date using DD-MM-YY')
    time = models.CharField(max_length=5, default=datetime.now, choices=TIME_CHOICES, help_text="Please select a time")
    status = models.IntegerField(choices=STATUS, default=0)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    
    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"{self.date} at {self.time} for {self.guests} people"


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
        return f"Comment {self.body} by {self.name}"

# class ManageBooking(models.Model):
#     number_of_tables = models.IntegerField
#     number_of_guests = models.IntegerField
#     date = models.DateField(default=datetime.now)
#     time = models.TimeField(default=datetime.now)


