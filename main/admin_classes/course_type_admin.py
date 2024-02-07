from django.contrib import admin
from .base_admin import BaseAdmin
from django import forms
from django_select2.forms import Select2Widget

from ..model_classes import (
    CourseType,
    Certificate
)

class CourseTypeAdminForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'
        widgets = {
            'certificate': Select2Widget,
        }
        required = {
            'certificate': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['certificate'].choices = [(certificate.id, str(certificate)) for certificate in Certificate.objects.all()]

    certificate = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class CourseTypeAdmin(BaseAdmin):
    form = CourseTypeAdminForm
    exclude = ['id', 'created_at', 'updated_at']


admin.site.register(CourseType, CourseTypeAdmin)
