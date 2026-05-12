from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pokedex import views


app_name = 'pokedex' 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('pokemon/<str:pokemon>/', views.pokemon, name='pokemon'),
    path('trainer/<int:id>/', views.trainer, name='trainer'),
    path('addPokemon/', views.addPokemon, name='addPokemon'),
    path('editPokemon/<int:id>/', views.editPokemon, name='editPokemon'),
    path('deletePokemon/<int:id>/', views.deletePokemon, name='deletePokemon'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)