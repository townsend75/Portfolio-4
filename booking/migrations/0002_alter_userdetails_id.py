# Generated by Django 3.2.22 on 2023-10-23 14:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
