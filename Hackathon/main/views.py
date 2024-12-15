from .models import School, Course, Review, Lesson
from .serializers import SchoolSerializer, CourseSerializer, ReviewSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Class, Lesson
from .serializers import CourseSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render, get_object_or_404
from rest_framework import filters


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer

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
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'school__name']
    ordering_fields = ['name', 'start_date', 'school__name']

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
    schools = School.objects.all()[:5] #get the first 5 schools
    return render(request, "home.html", {'courses': courses, 'schools':schools})

def schoollist(request):
    schools = School.objects.all()
    return render(request, 'schools.html', {'schools':schools})

def explore(request):
    return render(request, "explore.html")
   


# View for course lists Deprecated:

# class CourseListView(APIView):
#     def get(self, request):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CourseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def course_detail(request, course_id):
    courses = Course.objects.get(course_id=course_id)
    classes = Class.objects.all()
    return render(request, 'course_detail.html', {
        'course': courses, 
        'classes': classes
        })


def class_details(request, class_id):
    class_obj = get_object_or_404(Class, class_id=class_id)
    lessons = class_obj.lessons.all()
    return render(request, 'class_details.html', {
        'class_obj': class_obj,
        'lessons': lessons
    })


def lesson_detail(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})

def lesson_content(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    return render(request, 'lesson_content.html', {'lesson': lesson})

def school_detail(request, school_id):
    school = get_object_or_404(School, id=school_id)
    courses = school.courses.all()
    return render(request, 'school_detail.html', {
        'school': school,
        'courses': courses
        })

