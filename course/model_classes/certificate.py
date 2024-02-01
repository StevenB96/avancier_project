from djongo import models
from .base_model import BaseModel


class Certificate(BaseModel):
    course_type_id = models.CharField(max_length=255, blank=True, null=True)
    certificate_code = models.CharField(max_length=255, blank=True, null=True)
    certificate_name = models.CharField(max_length=255, blank=True, null=True)
    certification_body = models.CharField(max_length=255, blank=True, null=True)
    link_to_syllabus = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.certificate_name) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Certificates'
        db_table = 'certificate'