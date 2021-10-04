from rest_framework import serializers
from carros.models import Automovel, Marca


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automovel
        fields = '__all__'


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nome', 'origem']

class ListarCarrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automovel
        fields = ['id', 'nome', 'origem', 'ano']


