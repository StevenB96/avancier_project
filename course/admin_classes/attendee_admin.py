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
            'bookinginvoice': Select2Widget,
            'course': Select2Widget
        }
        required = {
            'bookinginvoice': False,
            'course': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['bookinginvoice'].choices = [(bookinginvoice.id, str(
            bookinginvoice)) for bookinginvoice in Bookinginvoice.objects.all()]
        self.fields['course'].choices = [
            (course.id, str(course)) for course in Course.objects.all()]

    bookinginvoice = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )
    course = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class AttendeeAdmin(BaseAdmin):
    form = AttendeeAdminForm
    exclude = []


admin.site.register(Attendee, AttendeeAdmin)
