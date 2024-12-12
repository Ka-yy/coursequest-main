from rest_framework import serializers
from .models import School, Course, Review

# Reviews
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
# Courses
class CourseSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'Title', 'description', 'Summary', 'reviews']
# Schools
class SchoolSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    
    class Meta:
        model = School
        fields = ['id', 'name', 'location', 'year_established', 'description', 'image', 'courses']
