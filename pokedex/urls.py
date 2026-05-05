from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 👈 tu lista de pokemons
    path('pokemon/<str:pokemon>/', views.pokemon, name='pokemon'),
]