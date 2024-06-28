from . import models
from rest_framework import serializers


class WarehouseSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = models.Warehouse
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Product
        fields  = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Category
        fields  = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Unit
        fields  = '__all__'

class BrandSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = models.Brand
        fields  = '__all__'

class ManufactureSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = models.Manufacture
        fields  = '__all__'


class TypeVariationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = models.TypeVariation
        fields = '__all__'
        