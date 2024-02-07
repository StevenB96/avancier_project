from django.db import models
from .address import Address
from .company import Company


class Contact(models.Model):
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
    )
    companies = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name_plural = 'Contacts'
        db_table = 'contact'
        managed = True
