from django.contrib import admin
from .base_admin import BaseAdmin
from django import forms
from django_select2.forms import Select2Widget

from ..model_classes import (
    Attendee,
    Bookinginvoice,
    Course,
)


class AttendeeAdminForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = '__all__'
        widgets = {
            'bookinginvoice_id': Select2Widget,
            'course_id': Select2Widget
        }
        required = {
            'bookinginvoice_id': False,
            'course_id': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['bookinginvoice_id'].choices = [(bookinginvoice._id, str(
            bookinginvoice)) for bookinginvoice in Bookinginvoice.objects.all()]
        self.fields['course_id'].choices = [
            (course._id, str(course)) for course in Course.objects.all()]

    bookinginvoice_id = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )
    course_id = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class AttendeeAdmin(BaseAdmin):
    form = AttendeeAdminForm
    exclude = ['_id']


admin.site.register(Attendee, AttendeeAdmin)
