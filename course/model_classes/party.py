from django.db import models
from django.utils import timezone


class Party(models.Model):
    email_address = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    approved_supplier_details = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name_plural = 'Parties'
        db_table = 'party'
        managed = True
