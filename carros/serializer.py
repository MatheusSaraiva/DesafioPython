from rest_framework import serializers
from carros.models import Carro, Marca


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ['nome', 'km_por_galao', 'cilindros', 'cavalor_de_forca', 'peso', 'aceleracao', 'ano', 'origem']
        extra_kwargs = {
            "km_por_galao": {'write_only': True},
            "cilindros": {'write_only': True},
            "cavalor_de_forca": {'write_only': True},
            "peso": {'write_only': True},
            "aceleracao": {'write_only': True},
        }


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['nome', 'origem']