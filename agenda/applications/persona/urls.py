from django.contrib import admin
from django.urls import path
from . import views

app_name = 'persona_app'
urlpatterns = [
    path('list_all/', views.PersonListView.as_view(), name='personas'),
    path('list_test/', views.PruebaListView.as_view(), name='personas2'),
    path('api/persona/lista/', views.PersonListApiView.as_view(),),
    path('api/persona/search/<kword>/', views.PersonSearchApiView.as_view(),),
    path('api/persona/create/', views.PersonCreateApiView.as_view(),),
    path('api/persona/detail/<pk>/', views.PersonDetailApiView.as_view(),name='detail'),
    path('api/persona/delete/<pk>/', views.PersonDeleteApiView.as_view(),),
    path('api/persona/update/<pk>/', views.PersonUpdateApiView.as_view(),),
    path('api/persona/showupdate/<pk>/', views.PersonRetrieveUpdateApiView.as_view(),),
    path('api/persona/lista_pag/', views.PersonPagListApiView.as_view(),),
    path('api/persona/lista2/', views.PersonListApiView2.as_view(),),
    path('api/reunion/lista/', views.MeetingListApiView.as_view(),),
    path('api/reunion/lista2/', views.MeetingListApiView2.as_view(),),
    path('api/reunion/lista_link/', views.MeetingListLinkApiView.as_view(),),
    path('api/reunion/by_job/', views.MeetingByJobApiView.as_view(),),
]