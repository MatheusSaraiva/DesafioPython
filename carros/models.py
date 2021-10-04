from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    origem = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.nome

class Automovel(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    km_por_galao = models.FloatField()
    cilindros = models.IntegerField()
    cavalor_de_forca = models.IntegerField()
    peso = models.FloatField()
    aceleracao = models.FloatField()
    ano = models.DateField()
    origem = models.CharField(max_length=255)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.nome






