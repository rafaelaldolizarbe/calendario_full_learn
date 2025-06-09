from django.shortcuts import render, redirect , get_object_or_404
from atividades.entityes.atividade import Atividade
from django.contrib.auth.decorators import login_required

# Login required decorator can be used if needed


@login_required
def calendario_view(request):
    atividades = Atividade.objects.all()
    return render(request, 'atividades/calendario.html', {'atividades': atividades})
@login_required
def novo_evento_view(request):

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        cor = request.POST.get('cor', '#3788d8')
        if titulo and data_inicio and data_fim:
            atividade = Atividade.objects.create(
                titulo=titulo,
                descricao=descricao,
                data_inicio=data_inicio,
                data_fim=data_fim,
                cor=cor
            )
            return redirect('novoevento')  # Redireciona para evitar reenvio do formul�rio

    eventos = Atividade.objects.all()
    return render(request, 'atividades/novo_evento.html', {'eventos': eventos})

@login_required
def editar_evento_view(request,evento_id):
    evento = get_object_or_404(Atividade, id=evento_id)
    if request.method == 'POST':
        evento.titulo = request.POST.get('titulo')
        evento.descricao = request.POST.get('descricao')
        evento.data_inicio = request.POST.get('data_inicio')
        evento.data_fim = request.POST.get('data_fim')
        evento.cor = request.POST.get('cor', '#3788d8')
        evento.save()
        return redirect('editarevento',evento_id=evento.id)
    eventos = Atividade.objects.all()
    return render(request, 'atividades/editar_evento.html', {'evento': evento, 'eventos':eventos})

