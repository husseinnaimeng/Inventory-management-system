class JsonObjectManager:
    
    def __init__(self,data: dict):
        
        self.data = data
        
    
    def has_item(self,key):
        
        if self.data.get(key,None):
            
            return True

        return False
    
    def get_item(self,key):
        
        return self.data.get(key,None)
    
    
    def add_item(self,key,value) -> dict:
        
        if not self.data.get(key,None):
            self.data[key] = value

        return self.data
    

    
    def remove_item(self,key):
        
        if self.data.get(key,None):
            
            del self.data[key]
        
        return self.data
    

# DictToObject is a class to turn dictonary into an object 
# So we can use dot-notation to use the keys,values as (attrubtes and values ) 
# Example 
#input:  data = DictToObject(data={'name':'Hussein Naim'})
# Inseted of accssing the dict object using keys 
# Now we can call the attrubte dirctly  from the class instance 
# data.name : output = 'Hussein Naim"

class DictToObject:
    
    def __init__(self,data: dict):
        
        self.data = data
        
        for key,value in self.data.items():
            
            setattr(self,key,value)

    # We can use this method to avoid attrubte errors 
    def get(self,attrubte : str ):
        
        if hasattr(self,attrubte):
            
            return getattr(self,attrubte)
        
        return None
