from djongo import models
from .course import Course
from .hotel import Hotel
from .base_model import BaseModel


class Venue(BaseModel):
    courses = models.ArrayField(model_container=Course)
    hotels = models.ArrayField(model_container=Hotel)

    address_id = models.CharField(max_length=255, blank=True, null=True)
    venue_name = models.CharField(max_length=255, blank=True, null=True)
    venue_contact_name = models.CharField(
        max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.venue_name) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Venues'
        db_table = 'venue'
