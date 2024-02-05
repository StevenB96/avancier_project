from django.contrib import admin
from .base_admin import BaseAdmin

from ..model_classes import (
    CourseType,
)


class CourseTypeAdmin(BaseAdmin):
    exclude = ['_id', 'enquiries', 'courses', 'certificates']


admin.site.register(CourseType, CourseTypeAdmin)
