from rest_framework import viewsets, filters
from carros.models import Carro, Marca
from carros.serializer import CarroSerializer, MarcaSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CarrosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os carros"""
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']
    filterset_fields = ['origem']

class MarcaViewSet(viewsets.ModelViewSet):
    """Exibindo todos as marcas"""
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']
    filterset_fields = ['origem']