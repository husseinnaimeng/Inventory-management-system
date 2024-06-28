from rest_framework import serializers

class Field:
    def __init__(self,name: str,field):
        setattr(self,name,field)


PRE_DEFIEND_TYPES = []


