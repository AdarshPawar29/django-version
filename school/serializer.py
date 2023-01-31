from rest_framework import serializers
from .models import Student, Teacher, Subject, Enrollment


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        depth = 1
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        depth = 1
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        depth = 1
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        depth = 1
        fields = ['student', 'subject']
