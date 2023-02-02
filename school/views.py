
from rest_framework.decorators import parser_classes
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import ClassRoom, Student, Teacher, Subject, Enrollment
from .serializer import ClassRoomSerializer, StudentSerializer, TeacherSerializer, SubjectSerializer, EnrollmentSerializer
from django.views.decorators.csrf import csrf_exempt
import json
from django.forms.models import model_to_dict
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
                reversion.set_comment(f"1st created version")
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
        for version in versions:
            print("version->>", version.field_dict)
            # print("versions comment->>", version.revision.comment)

        # print("versions->>", versions)
        # print("versions->>", versions[2].field_dict)
        print("versions comment->>", versions[0].revision.comment)
        # print("active version ->>", reversion.is_active())
        # versions[2].revision.revert()
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
        with reversion.create_revision():
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
        versions = Version.objects.get_for_object(teacher)
        for version in versions:
            print("version->>", version.field_dict)
            # print("versions comment->>", version.revision.comment)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        with reversion.create_revision():
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

        with reversion.create_revision():
            if serializer.is_valid():
                serializer.save()

                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)

    if request.method == 'GET':
        serializer = SubjectSerializer(subject)
        versions = Version.objects.get_for_object(subject)
        for version in versions:
            print("version->>", version.field_dict)
        # print("versions comment->>", version.revision.comment)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        with reversion.create_revision():
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
        with reversion.create_revision():
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
        versions = Version.objects.get_for_object(enrollment)
        for version in versions:
            print("version->>", version.field_dict)
            # print("versions comment->>", version.revision.comment)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        with reversion.create_revision():
            serializer = EnrollmentSerializer(enrollment, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        enrollment.delete()
        return HttpResponse(status=204)


@csrf_exempt
def class_room_list(request):
    if request.method == 'GET':
        classRoom = ClassRoom.objects.all()
        serializer = ClassRoomSerializer(classRoom, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        with reversion.create_revision():
            serializer = ClassRoomSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                reversion.set_comment(f"1st created version")
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def class_room_detail(request, pk):
    classRoom = get_object_or_404(ClassRoom, pk=pk)
    if request.method == 'GET':
        serializer = ClassRoomSerializer(classRoom)
        versions = Version.objects.get_for_object(classRoom)
        for version in versions:
            print("version->>", version.field_dict)
            print("versions comment->>", version.revision.comment)
        # versions[0].revision.revert()
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        with reversion.create_revision():
            serializer = ClassRoomSerializer(classRoom, data=data)
            if serializer.is_valid():
                serializer.save()
                reversion.set_comment(f"1st created version")
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        classRoom.delete()
        return HttpResponse(status=204)


def classroom_versions(request, pk):
    classRoom = get_object_or_404(ClassRoom, pk=pk)
    # revisions = Version.objects.get_for_object(classRoom)
    revisions = Version.objects.get_for_object(classRoom)

    # Create a list of versions
    versions = []
    for revision in revisions:
        version_data = revision.field_dict
        teacher_id = version_data.get("teacher_id")
        t_data = get_object_or_404(Teacher, pk=teacher_id)
        version_data['teacher_data'] = model_to_dict(t_data)
        version_data['versionId'] = revision.id
        version_data['database'] = revision.db
        version_data['serialized_data'] = revision.serialized_data
        versions.append(version_data)

    # Return the versions as a JSON response
    return JsonResponse({'versions': versions})


def classroom_versions_revert(request, pk, version_id):
    classRoom = get_object_or_404(ClassRoom, pk=pk)
    # revisions = Version.objects.get_for_object(classRoom)
    revisions = Version.objects.get_for_object(classRoom)
    if version_id > len(revisions):
        return HttpResponse(status=404)

    revisions[version_id].revision.revert()
    results = revisions[version_id].field_dict
    teacher_id = results.get("teacher_id")
    t_data = get_object_or_404(Teacher, pk=teacher_id)
    results['teacher_data'] = model_to_dict(t_data)

    return JsonResponse({'versions':  results})
