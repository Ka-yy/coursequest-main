from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'schools', views.SchoolViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'reviews', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.home, name='home'),
    path('courses/', views.Course, name='courses'),
    path('schools/', views.School, name='schools')
]


