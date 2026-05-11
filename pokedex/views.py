from django.shortcuts import render, get_object_or_404
from .models import Pokemon, Trainer

def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    return render(request, 'index.html', {'pokemons': pokemons, 'trainers': trainers})

def pokemon(request, pokemon):
    pokemon_obj = get_object_or_404(Pokemon, name=pokemon)
    return render(request, 'display_pokemon.html', {'pokemon': pokemon_obj})

def trainer(request, id):
    trainer_obj = get_object_or_404(Trainer, id=id)
    return render(request, 'display_trainer.html', {'trainer': trainer_obj})