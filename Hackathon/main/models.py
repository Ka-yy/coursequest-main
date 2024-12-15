from django.db import models
import uuid

def generate_unique_id():
    return str(uuid.uuid4())[:8]

class School(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    course_id = models.CharField(max_length=20, primary_key=True, unique=True, default=generate_unique_id)
    school = models.ForeignKey(School, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    summary = models.TextField()
    outline = models.TextField()

    def __str__(self):
        return self.title

class Class(models.Model):
    class_id = models.CharField(max_length=20, primary_key=True, unique=True, default=generate_unique_id)
    course = models.ForeignKey(Course, related_name='classes', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)  # For maintaining class order within a course

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    class Meta:
        verbose_name_plural = "Classes"
        ordering = ['order']

class Lesson(models.Model):
    lesson_id = models.CharField(max_length=20, primary_key=True, unique=True, default=generate_unique_id)
    class_obj = models.ForeignKey(Class, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.IntegerField(default=0)  # For maintaining lesson order within a class
    duration = models.DurationField(null=True, blank=True)  # Optional lesson duration

    def __str__(self):
        return f"{self.class_obj.title} - {self.title}"

    class Meta:
        ordering = ['order']

class Review(models.Model):
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)
    # Add other review-related fields as needed