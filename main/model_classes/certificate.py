from django.db import models


class Certificate(models.Model):
    # ATTRIBUTES FIELDS
    name = models.CharField(max_length=255)
    certification_body = models.CharField(max_length=255)    
    certificate_code = models.CharField(max_length=255)
    link_to_syllabus = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name_plural = 'Certificates'
        db_table = 'certificate'
        managed = True
