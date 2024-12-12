from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import School, Course, Review
from .serializers import SchoolSerializer, CourseSerializer, ReviewSerializer
from  django.shortcuts import render

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Course.objects.all()
        school_id = self.request.query_params.get('school', None)
        if school_id:
            queryset = queryset.filter(School_id=school_id)
        return queryset

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


def home(request):
    return render(request, "start.html")

def schoolhome(request):
    return render(request, "schoolhome.html")