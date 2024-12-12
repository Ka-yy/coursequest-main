from .models import School, Course, Review
from .serializers import SchoolSerializer, CourseSerializer, ReviewSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render, get_object_or_404


#SChools
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Courses 
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

# reviews
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


def home(request):
    courses = Course.objects.all()[:5] #get the first 5 courses
    schools = School.objects.all()[:5] #get the
    return render(request, "home.html", {'courses': courses, "schools":School})


def schoolhome(request):
    return render(request, "schools.html")

def explore(request):
    return render(request, "explore.html")
   


# View for course lists
class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})

def school_detail(request, school_id):
    school = get_object_or_404(School, id=school_id)
    return render(request, 'school_detail.html', {'school': school})