from django.contrib import admin
from .base_admin import BaseAdmin
from django import forms
from django_select2.forms import Select2Widget

from ..model_classes import (
    Venue,
    CourseType,
    Course
)


class CourseAdminForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'venue': Select2Widget,
            'course_type': Select2Widget
        }
        required = {
            'venue': False,
            'course_type': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['venue'].choices = [(venue.id, str(venue)) for venue in Venue.objects.all()]
        self.fields['course_type'].choices = [(course_type.id, str(course_type)) for course_type in CourseType.objects.all()]

    venue = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )
    course_type = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class CourseAdmin(BaseAdmin):
    form = CourseAdminForm
    exclude = []


admin.site.register(Course, CourseAdmin)
