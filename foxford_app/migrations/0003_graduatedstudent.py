# Generated by Django 5.0.6 on 2024-05-23 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foxford_app', '0002_alter_schedule_end_time_alter_schedule_start_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraduatedStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('image', models.ImageField(upload_to='foxford/g_student')),
                ('graduation_year', models.PositiveIntegerField()),
                ('band_score', models.CharField(max_length=10)),
            ],
        ),
    ]
