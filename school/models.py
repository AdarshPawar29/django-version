from django.db import models
from auditlog.registry import auditlog

# reversion
from django.contrib import admin
from reversion.admin import VersionAdmin
import reversion


# @reversion.register()
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)


auditlog.register(Student)  # to create a log of data


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, )
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="subjectTeacher")
    students = models.ManyToManyField(
        Student, through='Enrollment', related_name="subjectStudent")


class ClassRoom(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    students = models.ManyToManyField(
        Student, through='Enrollment', related_name="classStudent")
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="classTeacher")
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="classSubject")


class Enrollment(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="enrollmentStudent")
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="enrollmentSubject")
    classroom = models.ForeignKey(
        ClassRoom, on_delete=models.CASCADE, related_name="enrollmentClassRoom")
    date_enrolled = models.DateField(null=True)


reversion.register(
    Student, follow=["subjectStudent", "classStudent", "enrollmentStudent"])
reversion.register(
    Teacher, follow=["subjectTeacher", "classTeacher"])
reversion.register(Subject, follow=["classSubject", "enrollmentSubject"])
reversion.register(Enrollment)
reversion.register(ClassRoom, follow=["enrollmentClassRoom"])
