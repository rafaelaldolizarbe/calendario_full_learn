from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .entityes.atividade import Atividade
from .forms.admin_form import AtividadeAdminForm  # Importe o formulário criado acima

@admin.register(Atividade)
class AtividadeAdmin(SimpleHistoryAdmin):
    form = AtividadeAdminForm
    list_display = ('titulo', 'descricao', 'data_inicio', 'data_fim', 'cor')
