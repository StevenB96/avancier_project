from django.db import models
from django.utils import timezone
from .venue import Venue
from .course_type import CourseType


class Course(models.Model):
    venues = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
    )
    course_types = models.ForeignKey(
        CourseType,
        on_delete=models.CASCADE,
    )

    description = models.TextField(blank=True, null=True)
    attendee_total = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.description} - {self.id}"

    class Meta:
        verbose_name_plural = 'Courses'
        db_table = 'course'
        managed = True
