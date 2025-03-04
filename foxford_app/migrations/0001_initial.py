# Generated by Django 5.0.6 on 2024-05-22 13:40

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to='foxford/instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='foxford/course')),
                ('duration', models.IntegerField(help_text='Duration in weeks')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('publish_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('learning_outcomes', models.TextField(help_text='Separate each outcome with a newline')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='foxford_app.instructor')),
            ],
            options={
                'ordering': ['-publish_time'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('topic', models.CharField(max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='foxford_app.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('courses', models.ManyToManyField(related_name='students', to='foxford_app.course')),
            ],
        ),
    ]
