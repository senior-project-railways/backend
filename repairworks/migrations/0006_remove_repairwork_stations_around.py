# Generated by Django 4.1.3 on 2023-02-08 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repairworks', '0005_repairwork_stations_around'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repairwork',
            name='stations_around',
        ),
    ]
