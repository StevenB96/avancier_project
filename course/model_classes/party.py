from djongo import models
from .bookinginvoice import Bookinginvoice
from .enquiry import Enquiry
from .base_model import BaseModel


class Party(BaseModel):
    bookinginvoices = models.ArrayField(model_container=Bookinginvoice)
    enquiries = models.ArrayField(model_container=Enquiry)

    email_address = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    approved_supplier_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Parties'
        db_table = 'party'
        managed = True
