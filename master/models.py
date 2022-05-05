
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class course(models.Model):
    course_name = models.CharField(max_length=225)
    fee = models.IntegerField()

    def __str__(self):
        return self.course_name


class student(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE, null=True)
    std_name = models.CharField(max_length=225)
    std_address = models.CharField(max_length=225)
    std_age = models.IntegerField()

    def __str__(self):
        return self.course
