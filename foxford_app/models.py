from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='foxford/instructor')

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='foxford/course')
    duration = models.IntegerField(help_text="Duration in weeks")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_time = models.DateTimeField(auto_now_add=True)
    publish_time = models.DateTimeField(default=timezone.now)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')
    learning_outcomes = models.TextField(help_text="Separate each outcome with a newline")

    objects = models.Manager()

    class Meta:
        ordering = ['-publish_time']

    def __str__(self):
        return self.title

class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    topic = models.CharField(max_length=100)
    start_time = models.DateField()
    end_time = models.DateField()

    def __str__(self):
        return f"{self.course.title} - {self.topic} on {self.date}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class GraduatedStudent(models.Model):
    name = models.CharField(max_length=100)
    about=models.TextField()
    image = models.ImageField(upload_to='foxford/g_student')
    graduation_year = models.PositiveIntegerField()
    band_score = models.CharField(max_length=10)
    publish_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publish_time = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='foxford/blogs', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_time']