from django.db import models

# Create your models here.
class Bank(models.Model):
    acno=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    mobile=models.IntegerField()
    balance=models.IntegerField()