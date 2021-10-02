from django.test import TestCase
from carros.serializer import CarroSerializer
from carros.models import Carro


class CarroModelTestCase(TestCase):

    def setUp(self):
        self.carro = Carro(
            nome = 'JEEP COMPASS',
            km_por_galao = 10.1,
            cilindros = 4,
            cavalor_de_forca = 180,
            peso = 1544,
            aceleracao = 20,
            ano = '2018-08-10',
            origem = 'EUA'
        )
        self.serializer = CarroSerializer(instance=self.carro)

    def test_verifica_campos_serializados(self):
        """Teste verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['nome', 'ano', 'origem']))

    def test_verifica_conteudo_dos_campos_serializados(self):
        """Teste que verifica o conteudo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(data['nome'], self.carro.nome)
        self.assertEqual(data['ano'], self.carro.ano)
        self.assertEqual(data['origem'], self.carro.origem)
