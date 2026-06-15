from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from pokedex.models import Pokemon, Trainer
from .serializers import PokemonSerializer, TrainerSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticatedOrReadOnly]