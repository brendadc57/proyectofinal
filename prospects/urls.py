from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_prospects, name='lista'),
    path('nuevo/', views.crear_prospect, name='crear'),
]
