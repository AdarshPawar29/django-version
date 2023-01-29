from django.urls import path
from .views import student_list, student_detail, teacher_list, teacher_detail, subject_list, subject_detail, enrollment_list, enrollment_detail

urlpatterns = [
    path('students/', student_list, name='student-list'),
    path('students/<int:pk>/', student_detail, name='student-detail'),
    path('teachers/', teacher_list, name='teacher-list'),
    path('teachers/<int:pk>/', teacher_detail, name='teacher-detail'),
    path('subjects/', subject_list, name='subject-list'),
    path('subjects/<int:pk>/', subject_detail, name='subject-detail'),
    path('enrollments/', enrollment_list, name='enrollment-list'),
    path('enrollments/<int:pk>/', enrollment_detail, name='enrollment-detail'),
]
