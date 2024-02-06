from django.db import models
from django.utils import timezone
from .certificate import Certificate
from .course_type import CourseType


class CourseCertificate(models.Model):
    certificate = models.ForeignKey(
        Certificate,
        on_delete=models.CASCADE,
    )
    course_type = models.ForeignKey(
        CourseType,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name_plural = 'Course Certificates'
        db_table = 'course_certificate'
        managed = True
