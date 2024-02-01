from djongo import models
from .base_model import BaseModel


class Enquiry(BaseModel):
    course_type_id = models.CharField(max_length=255, blank=True, null=True)
    party_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.description) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Enquiries'
        db_table = 'enquiry'
