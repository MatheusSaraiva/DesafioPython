from rest_framework import serializers
from carros.models import Carro, Marca


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ['nome', 'km_por_galao', 'cilindros', 'cavalor_de_forca', 'peso', 'aceleracao', 'ano', 'origem']


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['nome', 'origem']