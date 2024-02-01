from djongo import models
from .base_model import BaseModel


class Hotel(BaseModel):
    venue_id = models.CharField(max_length=255, blank=True, null=True)
    address_id = models.CharField(max_length=255, blank=True, null=True)
    hotel_name = models.CharField(max_length=255, blank=True, null=True)
    hotel_website = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.hotel_name) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Hotels'
        db_table = 'hotel'
