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
    path('schools/', views.schoolhome, name='schoolhome'),
    path('explore/', views.explore, name='explore'),
    
    path('schools/', views.School, name='schools'),
    path('schoolhome/', views.schoolhome, name='Home'),
    path('api/', include(router.urls)),
    # for dynamic routes
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('school/<int:school_id>/', views.school_detail, name='school_detail'),
    path('courses', views.CourseListView, name='course_list' ),
    
]
