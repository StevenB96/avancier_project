from django.db import models
from .venue import Venue
from .course_type import CourseType


class Course(models.Model):
    # RELATIONSHIPS
    venues = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
    )
    course_types = models.ForeignKey(
        CourseType,
        on_delete=models.CASCADE,
    )
    # ATTRIBUTES FIELDS
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name_plural = 'Courses'
        db_table = 'course'
        managed = True

