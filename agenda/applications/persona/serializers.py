from rest_framework import serializers, pagination
from .models import Person, Meeting, Hobby


#*********** Hobby **********************************************************
class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ('__all__')

#*********** Person **********************************************************
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

class PersonSerializer3(serializers.ModelSerializer):
    # Para mostrar datos de relacion Many to Many
    hobby = HobbySerializer(many = True)
    class Meta:
        model = Person
        fields = (
            'id', 'full_name', 'job', 'email', 'phone','hobby'
        )
        
class PaginationSerializer(pagination.PageNumberPagination):
    """ Realiza la serialización por paginación """
    page_size = 5
    max_page_size = 100
        
#*********** Meeting **********************************************************
class MeetingSerializer(serializers.ModelSerializer):
    # Se le asigna al atributo 'person', su serializador, para que muestre todos los datos de este.
    person = PersonSerializer3()
    
    class Meta:
        model = Meeting
        fields = (
            'id', 'date', 'time', 'person'
        )
        
class MeetingSerializer2(serializers.ModelSerializer):
    # SerializerMethodField(), se utiliza para indicar que es un campo, que resulta de una operación. 
    # este campo no pertenece al modelo. Un ejemplo en (A)
    fecha_hora = serializers.SerializerMethodField()
    
    class Meta:
        model = Meeting
        fields = (
            'id', 'date', 'time', 'person', 'fecha_hora'
        )
    
    # (A)
    def get_fecha_hora(self, obj):
        return str(obj.date)+ ' - ' +str(obj.time)
    
class MeetingSerializerLink(serializers.HyperlinkedModelSerializer):
    """ Contiene un link a la info de persona """
    class Meta:
        model = Meeting
        fields = (
            'id', 'date', 'time', 'person'
        )
        extra_kwargs = {
            'person': {'view_name' : 'persona_app:detail', 'lookup_field': 'pk'}
        }

class MeetingCountSerializer(serializers.Serializer):
    """ Muestra reuniones por trabajo """
    person__job = serializers.CharField()
    cantidad = serializers.IntegerField()