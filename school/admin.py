from django.contrib import admin

# Register your models here.
from reversion.admin import VersionAdmin

from school.models import Enrollment, Student, Subject, Teacher
import reversion


class StudentAdmin(VersionAdmin):
    pass


class TeacherAdmin(VersionAdmin):
    pass


class SubjectAdmin(VersionAdmin):
    pass


class EnrollmentAdmin(VersionAdmin):
    pass


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
