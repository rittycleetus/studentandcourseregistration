from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=255)
    course_fees=models.IntegerField()




class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    student_name=models.CharField(max_length=255)
    student_email=models.EmailField()
    student_age=models.IntegerField()
    joining_date=models.DateField()