from django.db import models

# Create your models here.



class Users_info(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    mobileno=models.CharField(max_length=10)
    username=models.CharField(max_length=50,primary_key=True)
    password1=models.CharField(max_length=500)


