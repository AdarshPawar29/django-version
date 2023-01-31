from django.db import models
from auditlog.registry import auditlog

# reversion
from django.contrib import admin
from reversion.admin import VersionAdmin
import reversion


@reversion.register()
class Student(models.Model):
    pass
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)


auditlog.register(Student)  # to create a log of data


@reversion.register()
class Teacher(models.Model):
    pass
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='Enrollment')


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date_enrolled = models.DateField()
