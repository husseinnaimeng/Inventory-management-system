from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from .product_variation.product_varition import *

User = get_user_model()


def generate_inventory_name():
    count = Warehouse.objects.count() + 1
    return f'Inventory {count}'

class Warehouse(models.Model):

    admin = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='inventories')
    name = models.CharField(max_length=100, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = generate_inventory_name()
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        
        return self.name
    
    class Meta:
        
        permissions = [
            ('can_create_inventory',_('Can create inventory'))
        ]

# Product class

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    cost        = models.DecimalField(max_digits=10,decimal_places=3)
    sale_price  = models.DecimalField(max_digits=10,decimal_places=3)
    unit        = models.ForeignKey('Unit',on_delete=models.SET_NULL,null=True,related_name='unit_products')
    category    = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,related_name='category_products')
    demoinstions = models.CharField(max_length=100,help_text="Add product deminstions in this format (x*y*z)")
    brand       = models.ForeignKey("Brand",on_delete=models.SET_NULL,null=True,blank=True)
    manufacture = models.ForeignKey("Manufacture",on_delete=models.SET_NULL,null=True,blank=True)
    
    
    
    def profit_margin(self):
        
        percentage_profit = (self.sale_price / self.cost) * 100
        
        class ProfitInfo:
            def __init__(self,percentage,profit):
                self.percentage = percentage
                self.profit = profit
        
        return ProfitInfo(percentage_profit,self.sale_price - self.cost)
    



class ProductVariation(models.Model):
    product = models.ForeignKey(Product, related_name='variations', on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    quantity = models.IntegerField()
    

# Product spoecisifcations classes
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    



class Unit(models.Model):
    
    unit_name = models.CharField(max_length=10,unique=True)


class Brand(models.Model):
    
    name = models.CharField(max_length=100,unique=True)

class Manufacture(models.Model):
    
    name = models.CharField(max_length=100,unique=True)