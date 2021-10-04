from rest_framework import viewsets, filters
from carros.models import Automovel, Marca
from carros.serializer import CarroSerializer, MarcaSerializer, ListarCarrosSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class CarrosViewSet(viewsets.ModelViewSet):
    """
    get /carros/
    Listagem Colunas(id, nome, origem, ano)
            Filtros  (A search term == "nome") Origem(condição exata)
    """
    queryset = Automovel.objects.all()
    serializer_class = CarroSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']
    filterset_fields = ['origem']
    def list(self, request):

        queryset = Automovel.objects.all()
        queryset = self.filter_queryset(queryset)

        serializer = ListarCarrosSerializer(queryset, many=True)
        return Response(serializer.data)


class MarcaViewSet(viewsets.ModelViewSet):
    """
    get /marcas/
    Listagem Colunas(id, nome, origem)
            Filtros  (A search term == "nome") Origem(condição exata)
    """
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']
    filterset_fields = ['origem']

    def list(self, request):
        queryset = Automovel.objects.all()
        queryset = self.filter_queryset(queryset)

        serializer = MarcaSerializer(queryset, many=True)
        return Response(serializer.data)




