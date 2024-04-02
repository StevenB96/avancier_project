from django.db import models


class Company(models.Model):
    # ATTRIBUTES FIELDS
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name_plural = 'Companies'
        db_table = 'company'
        managed = True
