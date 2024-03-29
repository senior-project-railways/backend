# Generated by Django 4.1.3 on 2023-01-30 10:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainstations', '0002_alter_trainstation_latitude_and_more'),
        ('trains', '0004_remove_train_departure_remove_train_destination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='departureStation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departureStation', to='trainstations.trainstation'),
        ),
        migrations.AlterField(
            model_name='train',
            name='destinationStation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='destinationStation', to='trainstations.trainstation'),
        ),
        migrations.AlterField(
            model_name='train',
            name='latitude',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(90.0)]),
        ),
        migrations.AlterField(
            model_name='train',
            name='longitude',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)]),
        ),
    ]
