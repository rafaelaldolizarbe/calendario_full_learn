from django.urls import path
from .views.atividade_view import *

urlpatterns = [
    path('calendario/', calendario_view, name='calendario'),
    path('novoevento/', novo_evento_view, name='novoevento'),
    path('editarevento/<int:evento_id>/', editar_evento_view, name='editarevento'),
    ]
