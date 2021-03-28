from django.db import models
from Login.models import Users_info
# Create your models here.
class Bank(models.Model):
    acno=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    balance=models.IntegerField()
    status=models.IntegerField(null=True)
    username=models.ForeignKey(Users_info,on_delete=models.CASCADE,null=True)
    block=models.CharField(max_length=1,null=True)