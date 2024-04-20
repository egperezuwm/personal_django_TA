from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Types(models.TextChoices):
    Lecture = 'Lecture'
    Lab = 'Lab'

class Semesters(models.TextChoices):
    Fall = 'Fall'
    Spring = 'Spring'
    Summer = 'Summer'


class User(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=Roles)

    def __str__(self):
        return f"First Name: {self.first_name}, Last Name: {self.last_name}"


class Course(models.Model):
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=50)
    semester = models.CharField(max_length=50, choices=Semesters)
    year = models.IntegerField()

    def __str__(self):
        return f"Course Name: {self.course_name}, Semester: {self.semester}"


class Section(models.Model):
    section_id = models.IntegerField()
    # Days = ArrayField(models.CharField(max_length=50, choices=Days.choices), size=7)
    start_time = models.TimeField()
    end_time = models.TimeField()
    type = models.CharField(max_length=50, choices=Types)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course}-{self.section_id}"


class User_Course(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
