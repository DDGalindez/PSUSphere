from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("college_name",)  # Display college name in the list view
    search_fields = ("college_name",)  # Search by college name

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name", "college")  # Show program name and associated college
    search_fields = ("prog_name",)  # Search by program name

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "college", "description")  # Show organization details
    search_fields = ("name",)  # Search by organization name

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "program")  # List relevant fields
    search_fields = ("lastname", "firstname")  # Enable search by names

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "get_member_program", "organization", "date_joined")  # Show member details
    search_fields = ("student__lastname", "student__firstname")  # Enable search by student name

    def get_member_program(self, obj):
        try:
            return obj.student.program  # Directly access the program related to the student
        except Student.DoesNotExist:
            return None

    get_member_program.short_description = 'Program'  # Set column name in admin interface

