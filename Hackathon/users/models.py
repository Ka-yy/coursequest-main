from django.db import models
from django.core.validators import EmailValidator

class Users(models.Model):
    # personal details 
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(
        max_length=255,
        unique=True,
        validators=[EmailValidator()]
    )
    # login deatails 
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    # school details
    YEAR_CHOICES = [
        ('100', '100 Level'),
        ('200', '200 Level'),
        ('300', '300 Level'),
        ('400', '400 Level'),
        ('500', '500 Level'),
        ('600', '600 Level')
    ]
    # year 
    current_year = models.CharField(
        max_length=3,
        choices=YEAR_CHOICES,
        default='100'
    )

    #print the detials  
    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


    school = models.ForeignKey(
        'main.School',  
        on_delete=models.CASCADE,
        null=True,
        related_name='students'
    )
