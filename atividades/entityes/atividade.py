from simple_history.models import HistoricalRecords
from django.db import models

class Atividade(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    cor = models.CharField(max_length=7, default='#3788d8')  # Exemplo de cor padrão
    history = HistoricalRecords()  # <- Essa linha adiciona o log de auditoria

    def __str__(self):
        return self.titulo