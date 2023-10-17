from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField

STATUS = ( (0, "Unconfirmed"), (1, "Confirmed"))


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    number_of_guests = models.IntegerField
    date = models.DateField(default=datetime.now)
    time = models.TimeField(default=datetime.now)
    status = models.IntegerField(choices=STATUS, default=0)


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

