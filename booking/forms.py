from django.forms import ModelForm
from django import forms
from datetime import datetime
from .models import Person


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


class BookingForm(ModelForm):
    class Meta:
        model = Person
        fields = { 'name', 'email', 'guests', 'date', 'time'}
