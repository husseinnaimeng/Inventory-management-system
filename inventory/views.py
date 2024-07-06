from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .json_object_manager import DictToObject
import json
from . import models,serializers

class ListCreateInventory(ListCreateAPIView):
    
    permission_classes = [IsAdminUser]
    queryset= models.Warehouse.objects.all()
    serializer_class = serializers.WarehouseSerializer
    

class RetrieveUpdateDestroyInventoryAPIView(RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsAdminUser]
    queryset = models.Warehouse.objects.all()
    serializer_class = serializers.WarehouseSerializer
    


class ListCreateTypeVariationAPIView(ListCreateAPIView):
    
    permission_classes = [IsAdminUser]
    queryset = models.TypeVariation.objects.all()
    serializer_class = serializers.TypeVariationSerializer
    
    def post(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        attributes = models.TypeVariation.objects.valid_attributes(request.data.get("attributes",None))
        
        if serializer.is_valid() and attributes.is_valid:
            
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        elif not attributes.is_valid:
            #! We deleted the "is_valid" key so the users can not change the response using pentesting tools 
            #! The result will only be managed inside the server 
            del attributes['is_valid']
            #? you can go to "product_variation.py" and see the valid_attributes method in the TypeVariationManager class 
            #? in this class we try to mimic the response of DRF serailizer and the way of handling the error messages 
            #? so the user | developer have a clear idea of what's going on
            
            return Response(attributes.data,status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListCreateProductAPIView(ListCreateAPIView):
    
    permission_classes = [IsAdminUser]
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    

