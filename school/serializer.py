from rest_framework import serializers
from .models import ClassRoom, Student, Teacher, Subject, Enrollment


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

    # def to_representation(self, instance):
    #     rep = super(TeacherSerializer, self).to_representation(instance)
    #     rep['name'] = instance.teacher.first_name
    #     return rep


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        depth = 1
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        depth = 1
        fields = '__all__'


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        depth = 1
        fields = '__all__'
