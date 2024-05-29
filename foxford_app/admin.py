from django.contrib import admin
from .models import Course, Instructor, Student, Schedule, GraduatedStudent, Blog


# Register your models here.
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['course','date','topic','start_time','end_time']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','price','publish_time']
    list_filter=['price','publish_time','created_time']
    search_fields = ['title','description']
    date_hierarchy = 'publish_time'
    ordering = ['publish_time']

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['id','name',]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','date_of_birth','email']
    list_filter = ['first_name','last_name','email',]
    search_fields = ['first_name','last_name']

@admin.register(GraduatedStudent)
class GraduatedAdmin(admin.ModelAdmin):
    list_display = ['name','band_score','graduation_year']
    list_filter = ['name','band_score','graduation_year']
    search_fields = ['name','band_score','about']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','author',]
    list_filter = ['title','author']
    search_fields = ['title','author','content']
