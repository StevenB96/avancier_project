from django.db import models
from django.utils import timezone
from .party import Party
from .course_type import CourseType


class Enquiry(models.Model):
    parties = models.ForeignKey(
        Party,
        on_delete=models.CASCADE,
    )
    course_types = models.ForeignKey(
        CourseType,
        on_delete=models.CASCADE,
    )

    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.description} - {self.id}"

    class Meta:
        verbose_name_plural = 'Enquiries'
        db_table = 'enquiry'
        managed = True
