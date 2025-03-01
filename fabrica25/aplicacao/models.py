from django.db import models

class Valores_Convertidos(models.Model):
    nome = models.CharField(max_length=100)
    moeda_de_origem = models.CharField(max_length=3)
    moeda_destino = models.CharField(max_length=3)
    valor_de_origem = models.DecimalField(max_digits=10, decimal_places=2)
    valor_destino = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.moeda_de_origem} para {self.moeda_destino}'
