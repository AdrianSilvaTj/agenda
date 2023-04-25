from django.shortcuts import render
from django.views.generic import ListView,TemplateView

from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView,
    UpdateAPIView,RetrieveUpdateAPIView
)

from .models import Meeting, Person
from .serializers import (
    PersonSerializer, PersonSimpleSerializer, PersonSerializer2,
    MeetingSerializer, PersonSerializer3, MeetingSerializer2,
    MeetingSerializerLink, PaginationSerializer, MeetingCountSerializer
)


class PersonListView(ListView):
    model = Person
    template_name = "persona/list_all.html"
    
    def get_queryset(self):
        return Person.objects.all()

class PruebaListView(TemplateView):
    template_name= 'persona/lista.html'
    
# ********* API VIEWS *********************************************************
# ***** Person *********************************************
class PersonListApiView(ListAPIView):
    """ Api Mostrar lista de todas las personas"""
    serializer_class = PersonSerializer
    
    def get_queryset(self):
        return Person.objects.all()

class PersonSearchApiView(ListAPIView):
    """ Api Mostrar lista por busqueda de todas las personas"""
    serializer_class = PersonSerializer
    
    def get_queryset(self):
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains = kword
        )
    
class PersonCreateApiView(CreateAPIView):
    serializer_class = PersonSerializer
    
class PersonDetailApiView(RetrieveAPIView):
    """ Es el equivalente al detailView """
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    
class PersonDeleteApiView(DestroyAPIView):
    """ Es el equivalente al deleteView """
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonUpdateApiView(UpdateAPIView):
    """ Es el equivalente al UpdateView """
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    
class PersonRetrieveUpdateApiView(RetrieveUpdateAPIView):
    """ Es el equivalente al UpdateView, pero muestra los datos """
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonListApiView2(ListAPIView):
    """ Vista para interactuar con serializadores """
    serializer_class = PersonSerializer3
    
    def get_queryset(self):
        return Person.objects.all()
    
class PersonPagListApiView(ListAPIView):
    """ Api Mostrar lista de todas las personas con paginación """
    serializer_class = PersonSerializer
    pagination_class = PaginationSerializer
    
    def get_queryset(self):
        return Person.objects.all()

# ***** Meeting *********************************************

class MeetingListApiView(ListAPIView):
    """ Vista para interactuar con serializadores """
    serializer_class = MeetingSerializer
    
    def get_queryset(self):
        return Meeting.objects.all()
    
class MeetingListApiView2(ListAPIView):
    """ Vista con Serializador que contiene un campo con una operación  """
    serializer_class = MeetingSerializer2
    
    def get_queryset(self):
        return Meeting.objects.all()
    
class MeetingListLinkApiView(ListAPIView):
    """ Vista con Serializador que contiene un campo con una operación  """
    serializer_class = MeetingSerializerLink
    
    def get_queryset(self):
        return Meeting.objects.all()

class MeetingByJobApiView(ListAPIView):
    """ Vista para contar reuniones por trabajos """
    serializer_class = MeetingCountSerializer
    
    def get_queryset(self):
        return Meeting.objects.meetings_job_count()
        #return Meeting.objects.meetings_by_asunto()