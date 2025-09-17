from rest_framework.serializers import ModelSerializer, SlugRelatedField
from rest_framework import serializers
from ..models import Pet
from ..models import Perdidos

class PetSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = ['nome', 'especie', 'castrado', 'genero', 'vacinado', 'peso', 'porte', 'raca', 'foto']
        read_only_fields = ['org']

class PerdidosSerializer(ModelSerializer):
    class Meta:
        model = Perdidos
        fields = ['nome', 'especie', 'local', 'caracteristicas', 'genero', 'foto']
        read_only_fields = ['dono']