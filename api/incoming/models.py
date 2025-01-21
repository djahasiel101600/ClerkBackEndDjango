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
    iar_date = models.DateField()
    supplier = models.CharField(max_length=255)
    particulars = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_received_coa = models.DateTimeField()
    delay_duration = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    remarks = models.CharField(max_length=255)