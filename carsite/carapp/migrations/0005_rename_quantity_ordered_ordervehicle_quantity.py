# Generated by Django 5.0.1 on 2024-03-11 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0004_vehicle_features'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordervehicle',
            old_name='quantity_ordered',
            new_name='quantity',
        ),
    ]