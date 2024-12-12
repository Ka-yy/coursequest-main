from django.db import models
# Create your models here.
# School models
class School(models.Model):
        name = models.CharField(max_length=255)
        location = models.CharField(max_length=255)
        year_established = models.IntegerField()
        description = models.TextField()
        image = models.CharField(max_length=255)
        # rating = models.IntegerField()
        def __str__(self):
                return self.name

class Course(models.Model):
    School = models.ForeignKey(School, related_name='courses', 
    on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)  
    description = models.TextField()
    Summary = models.TextField()
    def __str__(self):
           return self.Title
                                                                 
class Review(models.Model):
        course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)
