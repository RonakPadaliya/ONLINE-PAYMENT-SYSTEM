from django.db import models

# Create your models here.



class Users_info(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    mobile=models.CharField(max_length=10)
    username=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=500)
    status=models.IntegerField(default=0)
    upi_staus=models.IntegerField(default=0)
    upi=models.IntegerField(default=0)


