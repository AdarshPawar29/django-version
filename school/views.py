
from rest_framework.decorators import parser_classes
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Student, Teacher, Subject, Enrollment
from .serializer import StudentSerializer, TeacherSerializer, SubjectSerializer, EnrollmentSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import reversion
from reversion.models import Version, Revision, VersionQuerySet


@parser_classes([JSONParser])
@csrf_exempt
def student_list(request):
    print("->>>", request)
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        print("->>>", request)
        data = JSONParser().parse(request)
        # Declare a revision block.
        with reversion.create_revision():
            serializer = StudentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def student_detail(request, pk):
    print("->>>", request)
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        # Load a queryset of versions for a specific model instance.
        # print("->>", Version.objects.get_for_object(student))
        versions = Version.objects.get_for_object(student)
        print("versions->>", versions)
        # print("versions->>", versions[2].field_dict)
        print("versions comment->>", versions[0].revision.comment)
        print("active version ->>", reversion.is_active())
        versions[2].revision.revert()
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        with reversion.create_revision():  # created version here!
            serializer = StudentSerializer(student, data=data)
            if serializer.is_valid():
                serializer.save()
                # print("data->", data)
                reversion.set_comment(f"created version {data['email']}")
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)


@csrf_exempt
def teacher_list(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TeacherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == 'GET':
        serializer = TeacherSerializer(teacher)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TeacherSerializer(teacher, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        teacher.delete()
        return HttpResponse(status=204)


@csrf_exempt
def subject_list(request):
    if request.method == 'GET':
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)

    if request.method == 'GET':
        serializer = SubjectSerializer(subject)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SubjectSerializer(subject, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        subject.delete()
        return HttpResponse(status=204)


@csrf_exempt
def enrollment_list(request):
    if request.method == 'GET':
        enrollments = Enrollment.objects.all()
        serializer = EnrollmentSerializer(enrollments, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EnrollmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def enrollment_detail(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)

    if request.method == 'GET':
        serializer = EnrollmentSerializer(enrollment)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EnrollmentSerializer(enrollment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        enrollment.delete()
        return HttpResponse(status=204)
