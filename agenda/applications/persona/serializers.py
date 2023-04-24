from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')
        
        
class PersonSimpleSerializer(serializers.Serializer):
    """ Este serializador no esta casado a un modelo """
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    # 'activo', es un campo adicional que no esta en el modelo, se podria utilizar cuando
    # se necesite realizar operaciones adicionales
    activo = serializers.BooleanField(default=False, required=False)

class PersonSerializer2(serializers.ModelSerializer):
    """ Utilizando el ModelSerializaer, se le puede agregar campos adicionales """
    activo = serializers.BooleanField(default=False, required=False)
    class Meta:
        model = Person
        fields = ('__all__')