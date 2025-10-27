from django.shortcuts import render 
from .models import Tarefa
from django.http import HttpResponse 

def listar_tarefas(request):
    tarefas_salvas = Tarefa.objects.all()
    contexto = {
        "minhas_tarefas": tarefas_salvas 
}
    
    return render (request, 'tarefas/lista.httpl,' contexto) 

def adicionar_tarefa (request):
    if request.method = = 'POST': 
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        Tarefa.objects.create(titulo=titulo, descricao=cescricao)

    return redirect('lista_tarefas1') 
