from django.urls import path
from .views import IndexPageView,AboutPageView,\
    BlogPageView,TeacherPageView,CoursesPageView,\
    ContactPageView,CourseDetailView,\
    GraduatedStudentView,TeacherView,BlogDetailView,SearchView

urlpatterns=[
    path('',IndexPageView,name='home_page'),
    path('about/',AboutPageView,name='about_page'),
    path('blog/',BlogPageView,name='blog_page'),
    path('teacher/',TeacherPageView,name='teacher_page'),
    path('course/',CoursesPageView,name='course_page'),
    path('contact/',ContactPageView,name='contact_page'),
    path('course/<int:course_id>/', CourseDetailView, name='course_detail'),
    path('graduated-students/<int:student_id>/', GraduatedStudentView, name='graduated_students'),
    path('teacher/<int:teacher_id>/',TeacherView,name='teacher_detail'),
    path('blog/<int:pk>/', BlogDetailView, name='blog_detail'),
    path('search/',SearchView , name='search'),
    path('contact/', ContactPageView, name='contact'),
    # path('teachers/',TeachersListView,name='teachers_list')

]