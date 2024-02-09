from django.db import models
from .contact import Contact
from .course import Course


class Bookinginvoice(models.Model):
    # RELATIONSHIPS
    contacts = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
    )
    courses = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )
    # ATTRIBUTES FIELDS
    purchase_order_number = models.CharField(max_length=255, blank=True, null=True)
    purchase_reference = models.CharField(max_length=255, blank=True, null=True)
    avancier_invoice_number = models.CharField(max_length=255, blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)
    expenses = models.CharField(max_length=255, blank=True, null=True)
    payment_terms = models.CharField(max_length=255, blank=True, null=True)    
    description = models.TextField(blank=True, null=True)
    payment_method = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.purchase_order_number} - {self.id}"

    class Meta:
        verbose_name_plural = 'Bookinginvoices'
        db_table = 'bookinginvoice'
        managed = True
