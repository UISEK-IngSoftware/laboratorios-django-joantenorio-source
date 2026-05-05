from django.http import HttpResponse
from django.template import loader
from .models import Pokemon

def index(request):
    pokemons = Pokemon.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))