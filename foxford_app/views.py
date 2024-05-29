from django.shortcuts import render
from .models import Course, GraduatedStudent, Instructor, Blog
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
# Create your views here.
def IndexPageView(request):
    blogs = Blog.objects.all().order_by('-publish_time')[:9]
    courses=Course.objects.all().order_by('-publish_time')[:8]
    graduated_students=GraduatedStudent.objects.all().order_by('-publish_time')[:6]
    instructors=Instructor.objects.all()
    context={
        'courses':courses,
        'graduated_students':graduated_students,
        'instructors':instructors,
        'blogs':blogs,
    }
    return render(request,template_name='foxford/index.html',context=context)

def AboutPageView(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request,'foxford/about.html',context=context)





def BlogPageView(request):
    blogs = Blog.objects.all().order_by('-publish_time')
    courses = Course.objects.all().order_by('-publish_time')[:8]
    paginator = Paginator(blogs, 6)  # Show 6 blogs per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    popular_posts =Blog.objects.all().order_by('-publish_time')[:3]

    context = {
        'page_obj': page_obj,
        'popular_posts':popular_posts,
        'courses':courses,
    }
    return render(request, 'foxford/blog.html', context=context)




def TeacherPageView(request):
    courses = Course.objects.all()
    teachers = Instructor.objects.all()
    context = {
        'courses': courses,
        'teachers':teachers
    }
    return render(request,'foxford/teacher.html',context=context)

def CoursesPageView(request):
    courses=Course.objects.all()
    context={
        'courses':courses
    }
    return render(request,'foxford/course.html',context=context)

def ContactPageView(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request,'foxford/contact.html',context=context)



def CourseDetailView(request, course_id):
    courses = Course.objects.all().order_by('-publish_time')[:8]
    course = get_object_or_404(Course, id=course_id)
    teachers=Instructor.objects.all()
    context = {
        'course': course,
        'courses':courses,
        'teachers':teachers,
    }
    return render(request, 'foxford/course_detail.html', context)

def GraduatedStudentView(request,student_id):
    g_student=get_object_or_404(GraduatedStudent,id=student_id)
    courses = Course.objects.all().order_by('-publish_time')[:8]
    context={
        'student':g_student,
        'courses':courses
    }
    return render(request,'foxford/graduated_student.html',context=context)

def TeacherView(request,teacher_id):
    teacher_view=get_object_or_404(Instructor,id=teacher_id)
    courses = Course.objects.all().order_by('-publish_time')[:8]
    context={
        'teacher_view':teacher_view,
        'courses':courses,

    }
    return render(request,'foxford/about_teacher.html',context=context)

def BlogDetailView(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    courses = Course.objects.all().order_by('-publish_time')[:8]
    return render(request, 'foxford/blog_detail.html', {'blog': blog,'courses':courses})


def SearchView(request):
    query = request.GET.get('q')
    courses = Course.objects.all().order_by('-publish_time')[:8]
    if query:
        blogs = Blog.objects.filter(title__icontains=query)
    else:
        blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
        'query': query,
        'courses':courses
    }
    return render(request, 'foxford/search_results.html', context)



