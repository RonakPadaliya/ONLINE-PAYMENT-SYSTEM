from django.db import models

# Create your models here.
class Bank(models.Model):
    customer_id=models.IntegerField(primary_key=True)
    account_no=models.IntegerField(max_length=14)
    ifsc_code=models.IntegerField(max_length=6)