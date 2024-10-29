from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        # Create Colleges and Programs if they don't exist
        self.create_colleges(5)   # Adjust the number of colleges as needed
        self.create_programs(10)  # Adjust the number of programs as needed
        self.create_organizations(10)
        self.create_students(50)
        self.create_memberships(10)

    def create_colleges(self, count):
        fake = Faker()
        for _ in range(count):
            College.objects.create(
                college_name=fake.company()
            )
        self.stdout.write(self.style.SUCCESS('Initial data for colleges created successfully.'))

    def create_programs(self, count):
        fake = Faker()
        colleges = College.objects.all()
        if colleges.exists():  # Ensure there are colleges available
            for _ in range(count):
                Program.objects.create(
                    prog_name=fake.word(),
                    college=colleges.order_by('?').first()
                )
            self.stdout.write(self.style.SUCCESS('Initial data for programs created successfully.'))
        else:
            self.stdout.write(self.style.WARNING('No colleges available to create programs.'))

    def create_organizations(self, count):
        fake = Faker()
        for _ in range(count):
            words = [fake.word() for _ in range(2)]  # two words
            organization_name = ' '.join(words)
            Organization.objects.create(
                name=organization_name.title(),
                college=College.objects.order_by('?').first(),
                description=fake.sentence()
            )
        self.stdout.write(self.style.SUCCESS('Initial data for organizations created successfully.'))

    def create_students(self, count):
        fake = Faker('en_PH')
        programs = Program.objects.all()
        if programs.exists():  # Ensure there are programs available
            for _ in range(count):
                Student.objects.create(
                    student_id=f"{fake.random_int(2020, 2024)}-{fake.random_int(1, 8)}-{fake.random_number(digits=4)}",
                    lastname=fake.last_name(),
                    firstname=fake.first_name(),
                    middlename=fake.last_name(),
                    program=programs.order_by('?').first()  # Ensure valid program
                )
            self.stdout.write(self.style.SUCCESS('Initial data for students created successfully.'))
        else:
            self.stdout.write(self.style.WARNING('No programs available to assign to students.'))

    def create_memberships(self, count):
        fake = Faker()
        students = Student.objects.all()
        organizations = Organization.objects.all()
        if students.exists() and organizations.exists():  # Ensure both exist
            for _ in range(count):
                OrgMember.objects.create(
                    student=students.order_by('?').first(),
                    organization=organizations.order_by('?').first(),
                    date_joined=fake.date_between(start_date="-2y", end_date="today")
                )
            self.stdout.write(self.style.SUCCESS('Initial data for student organization memberships created successfully.'))
        else:
            self.stdout.write(self.style.WARNING('Insufficient data to create memberships.'))
