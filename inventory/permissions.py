from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.apps import apps


app_config = apps.get_app_config('inventory')
models = app_config.get_models()

# List of model names
models = [model.__name__ for model in models]



def get_model_permissions(model: str) -> list[Permission]:


    content_type = ContentType.objects.get(app_label='Inventory', model=model.capitalize())

    # Get all permissions for the specified model
    permissions = Permission.objects.filter(content_type=content_type)

    # List of permission codes and names
    permissions_list = [(perm.codename, perm.name) for perm in permissions]

    return {'model':model,'permissions':permissions_list}



# class ModelPermssions:
    
#     def __init__(self,model: str) -> None:
        
#         for permission in get_model_permissions(model):
            
#             setattr(self,model,permission[0])


# permissions = [ModelPermssions(model) for model in models]