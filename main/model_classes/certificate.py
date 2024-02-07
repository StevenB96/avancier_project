from django.db import models


class Certificate(models.Model):
    certificate_code = models.CharField(max_length=255, blank=True, null=True)
    certificate_name = models.CharField(max_length=255, blank=True, null=True)
    certification_body = models.CharField(
        max_length=255, blank=True, null=True)
    link_to_syllabus = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.certificate_name} - {self.id}"

    class Meta:
        verbose_name_plural = 'Certificates'
        db_table = 'certificate'
        managed = True
