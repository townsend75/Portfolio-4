# Generated by Django 3.2.22 on 2023-10-19 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20231017_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='number_of_guests',
            field=models.IntegerField(default=0, help_text='Please enter the number of guests in your party'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.datetime.now, help_text='Please select a date using DD-MM-YY'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(help_text='Please provide a valid email address in case we need to contact you', max_length=254),
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(help_text='Please enter your full name', max_length=80),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(choices=[('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00')], default=datetime.datetime.now, help_text='Please select a time'),
        ),
    ]