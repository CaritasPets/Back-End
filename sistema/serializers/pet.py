from rest_framework.serializers import ModelSerializer, SlugRelatedField
from rest_framework import serializers
from ..models import Pet
from ..models import Perdidos

class PetSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'nome', 'especie', 'castrado', 'genero', 'vacinado', 'peso', 'porte', 'raca', 'foto', 'org']
        read_only_fields = ['org']
        depth = 1
class PerdidosSerializer(ModelSerializer):
    class Meta:
        model = Perdidos
        fields = ['id', 'nome', 'especie', 'local', 'caracteristicas', 'genero', 'foto', 'dono']
        read_only_fields = ['dono']
        depth = 1