# Generated by Django 5.0.6 on 2024-08-17 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
    ]
