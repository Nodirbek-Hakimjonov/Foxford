# Generated by Django 5.0.6 on 2024-05-23 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foxford_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.DateField(),
        ),
    ]
