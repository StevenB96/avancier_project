from django.db import models


class Enquiry(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.id}"

    class Meta:
        verbose_name_plural = 'Enquiries'
        db_table = 'enquiry'
        managed = True
