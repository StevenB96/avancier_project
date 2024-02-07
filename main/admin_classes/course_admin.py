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
            'venues': Select2Widget,
            'course_types': Select2Widget
        }
        required = {
            'venues': False,
            'course_types': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['venues'].choices = [(venues.id, str(venues)) for venues in Venue.objects.all()]
        self.fields['course_types'].choices = [(course_types.id, str(course_types)) for course_types in CourseType.objects.all()]

    venues = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )
    course_types = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class CourseAdmin(BaseAdmin):
    form = CourseAdminForm
    exclude = ['id', 'created_at', 'updated_at']


admin.site.register(Course, CourseAdmin)
