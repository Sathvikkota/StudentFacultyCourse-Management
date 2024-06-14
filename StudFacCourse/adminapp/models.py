

# Create your models here.
from django.db import models


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "admin_table"

    def __str__(self):
        return self.username


class Course(models.Model):
    id = models.AutoField(primary_key=True)

    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(Honors)"), ("CSIT", "CS&IT"))
    department = models.CharField(max_length=100, blank=False, choices=department_choices)

    program_choices = (("B.TECH", "Bachelor of Technology"), ("M.TECH", "Masters of Technology"),
                       ("MBA", "Master of Business Administration"))
    program = models.CharField(max_length=50, blank=False, choices=program_choices)

    academic_choices = (("2021-2022", "2021-2022"), ("2022-2023", "2022-2023"), ("2023-2024", "2023-2024"))
    academicyear = models.CharField(max_length=20, blank=False, choices=academic_choices)

    semester_choices = (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=False, choices=semester_choices)

    year_choices = ((1, 1), (2, 2), (3, 3), (4, 4))
    year = models.IntegerField(blank=False, choices=year_choices)

    coursecode = models.CharField(max_length=20, blank=False)
    coursetitle = models.CharField(max_length=100, blank=False)

    ltps=models.CharField(max_length=10,blank=False)
    credits=models.FloatField(blank=False)

    class Meta:
        db_table = "course_table"

    def __str__(self):
        return self.coursecode + " - " + self.coursetitle


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    studentid = models.BigIntegerField(blank=False, unique=True)
    fullname = models.CharField(max_length=100, blank=False)

    gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("OTHERS", "OTHERS"))
    gender = models.CharField(max_length=20, blank=False, choices=gender_choices)

    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(Honors)"), ("CSIT", "CS&IT"))
    department = models.CharField(max_length=50, blank=False, choices=department_choices)

    program_choices = (("B.TECH", "Bachelor of Technology"), ("M.TECH", "Masters of Technology"),
                       ("MBA", "Master of Business Administration"))
    program = models.CharField(max_length=50, blank=False, choices=program_choices)

    semester_choices = (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=False, choices=semester_choices)

    year_choices = ((1, 1), (2, 2), (3, 3), (4, 4))
    year = models.IntegerField(blank=False, choices=year_choices)  # 1 or 2 or 3 or 4
    password = models.CharField(max_length=100, blank=False, default="klu123")
    email = models.CharField(max_length=100, blank=False, unique=True)
    contact = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        db_table = "student_table"

    def __str__(self):
        return str(self.studentid)


class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    facultyid = models.BigIntegerField(blank=False, unique=True)
    fullname = models.CharField(max_length=100, blank=False)

    gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("OTHERS", "OTHERS"))
    gender = models.CharField(max_length=20, blank=False, choices=gender_choices)

    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(Honors)"), ("CSIT", "CS&IT"))
    department = models.CharField(max_length=50, blank=False, choices=department_choices)

    qualification_choices = (
    ("B.TECH", "Bachelor of Technology"), ("M.TECH", "Masters of Technology"), ("Ph.D", "Doctor of Philosophy"))
    qualification = models.CharField(max_length=50, blank=False, choices=qualification_choices)

    designation_choices = (
    ("Prof", "Professor"), ("Assoc.Prof", "Associate Professor"), ("Asst.Prof", "Assistant Professor"))
    designation = models.CharField(max_length=50, blank=False, choices=designation_choices)
    password = models.CharField(max_length=100, blank=False, default="klu123")
    email = models.CharField(max_length=100, blank=False, unique=True)
    contact = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        db_table = "faculty_table"

    def __str__(self):
        return str(self.facultyid) + " - " + self.fullname

class FacultyCourseMapping(models.Model):
    mappingid=models.AutoField(primary_key=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)

    component_choices=(("L","Lecture"),("T","Tutorial"),("P","Practical"),("S","Skill"))
    component=models.CharField(max_length=10,blank=False,choices=component_choices)

    type=models.BooleanField(blank=False,verbose_name="Faculty Type")
    section=models.IntegerField(blank=False)

    class Meta:
        db_table="facultycoursemapping_table"

    def __str__(self):
        return self.course.coursetitle+" - "+self.faculty.fullname
