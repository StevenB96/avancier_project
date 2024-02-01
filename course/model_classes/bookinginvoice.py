from djongo import models
from .attendee import Attendee
from .base_model import BaseModel


class Bookinginvoice(BaseModel):
    attendees = models.ArrayField(model_container=Attendee)

    party_id = models.CharField(max_length=255, blank=True, null=True)
    address_id = models.CharField(max_length=255, blank=True, null=True)
    course_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    payment_method = models.IntegerField(blank=True, null=True)
    po_or_ref_number = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.description) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Bookinginvoices'
        db_table = 'bookinginvoice'
