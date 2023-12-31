# Generated by Django 3.2.22 on 2023-10-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_userdetails_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='date',
            field=models.DateField(help_text='Please select a date using d-m-y'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='time',
            field=models.TimeField(help_text='Please select a time'),
        ),
    ]
