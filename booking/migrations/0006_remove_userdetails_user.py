# Generated by Django 3.2.22 on 2023-10-20 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20231019_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='user',
        ),
    ]
