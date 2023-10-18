from django import forms
from datetime import datetime

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


class BookingForm(forms.Form):
    name = forms.CharField(max_length=80, required=True)
    email = forms.EmailField(required=True)
    number_of_guests = forms.IntegerField
    date = forms.DateField
    time = forms.ChoiceField(choices=TIME_CHOICES)
