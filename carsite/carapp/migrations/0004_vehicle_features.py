# Generated by Django 5.0.1 on 2024-03-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0003_groupmember_alter_buyer_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='features',
            field=models.CharField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Auto Start / Stop', 'Auto Start / Stop')], default='Cruise Control', max_length=100),
        ),
    ]