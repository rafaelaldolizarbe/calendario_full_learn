from django import forms
from atividades.entityes.atividade import Atividade

class AtividadeAdminForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = '__all__'
        widgets = {
            'cor': forms.TextInput(attrs={'type': 'color'}),
        }