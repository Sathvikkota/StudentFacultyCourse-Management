from django.forms import forms

from .models import CourseContent


class AddCourseContent(forms.ModelForm):
    class Meta:
        model=CourseContent
        fields="__all__"