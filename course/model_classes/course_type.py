from django.db import models
from django.utils import timezone


class CourseType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    delivery_mode = models.IntegerField(blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name_plural = 'Course Types'
        db_table = 'course_type'
        managed = True
