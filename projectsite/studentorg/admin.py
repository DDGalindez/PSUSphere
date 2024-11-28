from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

# Register College
admin.site.register(College)

# Register Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "program")
    search_fields = ("lastname", "firstname", "student_id", "program__prog_name")

# Register OrgMember
@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "get_member_program", "organization", "date_joined")
    search_fields = ("student__lastname", "student__firstname")

    def get_member_program(self, obj):
        return obj.student.program  # Assuming `student` is a ForeignKey to `Student`.

    get_member_program.short_description = "Program"

# Register Organization
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "college", "description")
    search_fields = ("name", "college__college_name", "description")

# Register Program
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name", "get_college")
    search_fields = ("prog_name", "college__college_name")

    def get_college(self, obj):
        return obj.college.college_name  # Assuming `college` is a ForeignKey to `College`.

    get_college.short_description = "College"
