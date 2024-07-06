from django.db import models
from ..json_object_manager import DictToObject
import json


class ProductType(models.Model):
    name = models.CharField(max_length=100,unique=True)
    
    def get_type_variation(self):
        
        try:
            return self.type_variation.all()
        
        except:
            return []


class AttributesError:
    
    def __init__(self,data: dict):

        self.data = data
        
        if not "is_valid" in self.data :
            raise AttributeError("The data must contain a 'is_valid' key with a value ")
        
        for key,value in data.items():
            
            setattr(self,key,value)
        
    def __delitem__(self, key):
        del self.data[key]
    

class TypeVariationManager(models.Manager):
    
    def get_item(self,id: int , key : str):
        
        object = self.filter(id=id)
        
        if object.exists():
            object = object[0]
            
            attributes = object.attributes
            
            return dict(attributes).get(key,None)        
        
        return None

    def attributes_must_have(self,attributes: dict):
        must_have = ['quantity','price','field_type']
        
        for key in must_have:
            if not attributes.get(key,None):
                
                return {'pass':False,'error_message':f'The attributes field must have the key {key}  '}
                        
        
        return {'pass':True}
                
    def valid_attributes(self,attributes) -> bool:
        
        response = {"is_valid":False}
        error_messages = []
        
        try:
            attributes = json.loads(attributes)
            
            if isinstance(attributes,dict):
                
                for key,value in dict(attributes).items():
                    
                    if str(key).isnumeric() or str(key).isdecimal()  or str(key).isdigit() or str(key).isspace() or key == "":
                        error_messages.append("One of the keys is not a valid key")
                        break

                    else:
                        response['is_valid'] = True
                
                if not self.attributes_must_have(attributes).get("pass"):
                    response['is_valid'] = False
                    error_messages.append(self.attributes_must_have(attributes).get("error_message"))

            else:
                response['is_valid'] = False
                error_messages.append("invalid attributes  (the attributes field must be a dictonary consist of key and value ) ")
            
        except:
            
            response['is_valid'] = False
            error_messages.append("invalid attributes  (the attributes field must be a dictonary consist of key and value ) ")
        

        response['error_messages'] = error_messages
        
        return AttributesError(response)

    def update_item(self,id: int , key : str , value):
        
        object = self.filter(id=id) 
        
        if object.exists():
            
            object = object[0]
            
            attributes = dict(object.attributes)
            
            if attributes.get(key,None):
                
                attributes[key] = value
                
                new_attributes  = attributes
                
                object.attributes = new_attributes
                
                object.save()
                
                return DictToObject({'updated':True,'object':object})
            
            else:
                return DictToObject({'updated':False,'error_message':f'Object {object.__str__()} has no attribute called {key} ','error_code':'key_error'})     
        
        return DictToObject({'updated':False,'error_message':f'Object with ID({id}) was not found','error_code':'object_not_found'})

    def del_item(self,id: int,key: str):
        
        object = self.filter(id=id) 
        
        if object.exists():
            
            object = object[0]
            
            attributes = dict(object.attributes)
            
            if attributes.get(key,None):
                del attributes[key]

                new_attributes  = attributes
                
                object.attributes = new_attributes
                
                object.save()
                
                return DictToObject({'deleted':True,'object':object})
            else:
                return DictToObject({'deleted':False,'error_message':f'Object {object.__str__()} has no attribute called {key} ','error_code':'key_error'})
            
        
        return DictToObject({'deleted':False,'error_message':f'Object with ID({id}) was not found','error_key':'object_not_found'})
    
    def set_items(self,id:int,values : dict ):
        object = self.filter(id=id)
        
        if object.exists():
            
            object = object[0]
            
            object.attributes = values
            
            object.save()
            
            return DictToObject({'set':True,'object':object})
        
        else:
            
            return DictToObject({'set':False,'error_message':f'Object with ID({id}) was not found','error_code':'object_not_found'})

        


class TypeVariation(models.Model):
    product_type = models.ForeignKey(ProductType,on_delete=models.CASCADE,related_name='type_varition',blank=True,null=True)
    product = models.ForeignKey('inventory.Product',on_delete=models.CASCADE,related_name='product_variation')
    attributes = models.JSONField(default=dict,unique=True)
    objects = TypeVariationManager()
    
    def __str__(self):
        
        return f'Product Variation for {self.product.name}'

    def get_attrubtes(self):
        
        return DictToObject(self.attributes)