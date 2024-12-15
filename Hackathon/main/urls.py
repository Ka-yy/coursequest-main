from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'schools', views.SchoolViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'reviews', views.ReviewViewSet)

urlpatterns = [
    path('',views.home, name='home'),
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),

    # for static routes and beginning templates
    path('schools/', views.schoollist, name='school list'),
    path('explore/', views.explore, name='explore'),
    
    path('schools/', views.School, name='schools'),
    path('api/', include(router.urls)),
    # for dynamic routes
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('schools/<str:school_id>/', views.school_detail, name='school_detail'),
    path('courses/', views.course_list, name='courses' ),
    path('lesson-content/<int:lesson_id>/', views.lesson_content, name='lesson_content'),
    path('class/<strLclass_id>', views.class_details, name='class_detail'),
]

from django.shortcuts import render
from .models import Lesson
# import your ChatGPT integration module here
# what is my chatgpt integration module supposed to be
def lesson_content(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    
    # Placeholder for ChatGPT integration
    # if not lesson.content:
    #     lesson.content = generate_lesson_content_with_chatgpt(lesson.title)
    #     lesson.save()
    
    return render(request, 'lesson_content.html', {'lesson': lesson})