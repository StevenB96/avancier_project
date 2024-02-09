from django.db import models
from .certificate import Certificate


class CourseType(models.Model):
    # RELATIONSHIPS
    certificate = models.OneToOneField(
        Certificate,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    # ATTRIBUTES FIELDS
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField()
    delivery_mode = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name_plural = 'Course Types'
        db_table = 'course_type'
        managed = True
