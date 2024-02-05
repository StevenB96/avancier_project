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
            'venue_id': Select2Widget,
            'course_type_id': Select2Widget
        }
        required = {
            'venue_id': False,
            'course_type_id': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['venue_id'].choices = [(venue._id, str(venue)) for venue in Venue.objects.all()]
        self.fields['course_type_id'].choices = [(course_type._id, str(course_type)) for course_type in CourseType.objects.all()]

    venue_id = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )
    course_type_id = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class CourseAdmin(BaseAdmin):
    form = CourseAdminForm
    exclude = ['_id', 'bookinginvoices', 'attendees']


admin.site.register(Course, CourseAdmin)
