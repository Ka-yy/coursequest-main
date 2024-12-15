from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
class Course(models.Model):
    course_id = models.CharField(max_length=20, primary_key=True, unique=True, default=100)
    school = models.ForeignKey(School, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    summary = models.TextField()
    outline = models.TextField()
    def __str__(self):
        return self.title

class Review(models.Model):
        course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)


# delete this block later
class Class(models.Model):
    class_id = models.CharField(max_length=20, primary_key=True, unique=True, default=100)
    course = models.ForeignKey(Course, related_name='classes', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Lesson(models.Model):
    lesson_id = models.CharField(max_length=20, primary_key=True, unique=True, default=100)
    class_obj = models.ForeignKey(Class, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.class_obj.title} - {self.title}"
