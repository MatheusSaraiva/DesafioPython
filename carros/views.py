from rest_framework import viewsets
from carros.models import Carro, Marca
from carros.serializer import CarroSerializer, MarcaSerializer


class CarrosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os carros"""
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer


class MarcaViewSet(viewsets.ModelViewSet):
    """Exibindo todos as marcas"""
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
