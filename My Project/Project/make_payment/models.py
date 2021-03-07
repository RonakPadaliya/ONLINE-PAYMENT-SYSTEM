from django.db import models
import datetime
# Create your models here.
class Transaction(models.Model):
    Transaction_id=models.AutoField(primary_key=True)
    date=models.DateField(("Date"),default=datetime.date.today)
    sender_name=models.CharField(max_length=100)
    sender_mobile=models.CharField(max_length=10)
    sender_acno=models.CharField(max_length=14)
    sender_amount=models.IntegerField()
    sender_purpose=models.CharField(max_length=100000)
    receiver_name=models.CharField(max_length=100)
    receiver_mobile=models.CharField(max_length=10)
    receiver_acno=models.CharField(max_length=14)