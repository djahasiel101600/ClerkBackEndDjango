from django.db import models

# IAR Fields:
# IAR No.
# IAR Date
# Supplier
# Particulars
# Amount
# Date Received (COA OFfice)
# Delay Duration
# DateTime Created
# DateTime Updated
# Remarks
# Create your models here.
class IARRecord(models.Model):
    iar_no = models.CharField(max_length=16)
    iar_date = models.DateTimeField()
    supplier = models.CharField(max_length=255)
    particulars = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    sales_invoice_no = models.CharField(max_length=16)
    date_invoice = models.DateTimeField()
    date_received_officer = models.DateTimeField()
    date_acceptance = models.DateTimeField()
    date_inspection = models.DateTimeField()
    date_received_coa = models.DateTimeField()
    agency = models.CharField(max_length=255)
    delay_duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)