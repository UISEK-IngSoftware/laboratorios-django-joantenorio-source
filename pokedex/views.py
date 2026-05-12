from django.shortcuts import render, get_object_or_404, redirect
from .models import Pokemon, Trainer
from .forms import PokemonForm


def index(request):

    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()

    return render(request, 'index.html', {
        'pokemons': pokemons,
        'trainers': trainers
    })


def pokemon(request, pokemon):

    pokemon_obj = get_object_or_404(Pokemon, name=pokemon)

    return render(request, 'display_pokemon.html', {
        'pokemon': pokemon_obj
    })


def trainer(request, id):

    trainer_obj = get_object_or_404(Trainer, id=id)

    return render(request, 'display_trainer.html', {
        'trainer': trainer_obj
    })


def addPokemon(request):

    if request.method == 'POST':

        form = PokemonForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect('pokedex:index')

    else:

        form = PokemonForm()

    return render(request, 'pokemonForm.html', {
        'form': form
    })


def editPokemon(request, id):

    pokemon = get_object_or_404(Pokemon, id=id)

    if request.method == 'POST':

        form = PokemonForm(
            request.POST,
            request.FILES,
            instance=pokemon
        )

        if form.is_valid():

            form.save()

            return redirect('pokedex:index')

    else:

        form = PokemonForm(instance=pokemon)

    return render(request, 'pokemonForm.html', {
        'form': form
    })


def deletePokemon(request, id):

    pokemon = get_object_or_404(Pokemon, id=id)

    pokemon.delete()

    return redirect('pokedex:index')