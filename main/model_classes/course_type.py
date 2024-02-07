from django.db import models
from .certificate import Certificate


class CourseType(models.Model):
    certificate = models.OneToOneField(
        Certificate,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    delivery_mode = models.IntegerField(blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name_plural = 'Course Types'
        db_table = 'course_type'
        managed = True
