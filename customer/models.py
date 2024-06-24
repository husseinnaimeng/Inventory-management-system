from django.db import models


class Customer(models.Model):
    
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True,max_length=100)
    phone = models.CharField(max_length=11,unique=True)    
    address = models.CharField(max_length=200)
    
