from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pokedex import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('pokemon/<str:pokemon>/', views.pokemon, name='pokemon'),
    path('trainer/<int:id>/', views.trainer, name='trainer'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)