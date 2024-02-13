from django.contrib import admin
from .base_admin import BaseAdmin
from django import forms
from django_select2.forms import Select2Widget

from ..model_classes import (
    Attendee,
    Course,
)


class AttendeeAdminForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = '__all__'
        widgets = {
            'courses': Select2Widget,
        }
        required = {
            'courses': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['courses'].choices = [
            (course.id, str(course))
            for course in Course.objects.all()]


class AttendeeAdmin(BaseAdmin):
    form = AttendeeAdminForm
    exclude = ['id', 'created_at', 'updated_at']


admin.site.register(Attendee, AttendeeAdmin)
