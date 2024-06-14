from django import forms
from .models import Faculty, Student

class AddFacultyForm(forms.ModelForm):
    class Meta:
        model=Faculty
        fields="__all__"
        exclude={"password"}
        labels={"facultyid":"Enter Faculty ID","fullname":"Faculty Name","gender":"Select Gender","department":"Select Department",
                "qualification":"Select Qualification","designation":"Select Designation"}

class AddStudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        exclude={"password"}
        labels={"studentid":"Enter Student ID","fullname":"Student Name"}
