# Generated by Django 4.1.3 on 2023-01-26 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairworks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairwork',
            name='status',
            field=models.CharField(choices=[('Waiting for confirmation', 'Waiting'), ('In progress', 'In Progress'), ('Finished', 'Finished')], default='Waiting for confirmation', max_length=25),
        ),
    ]