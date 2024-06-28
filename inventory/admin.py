from django.contrib import admin
from . import models

admin.site.register(models.Warehouse)
admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.ProductType)
admin.site.register(models.TypeVariation)
admin.site.register(models.Unit)