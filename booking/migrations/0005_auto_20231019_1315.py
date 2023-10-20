# Generated by Django 3.2.22 on 2023-10-19 13:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0004_auto_20231019_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Please enter your full name', max_length=80)),
                ('email', models.EmailField(help_text='Please provide a valid email address in case we need to contact you', max_length=254)),
                ('number_of_guests', models.IntegerField(default=0, help_text='Please enter the number of guests in your party')),
                ('date', models.DateField(default=datetime.datetime.now, help_text='Please select a date using DD-MM-YY')),
                ('time', models.CharField(choices=[('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00')], default=datetime.datetime.now, help_text='Please select a time', max_length=5)),
                ('status', models.IntegerField(choices=[(0, 'Unconfirmed'), (1, 'Confirmed')], default=0)),
                ('confirmed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]