from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Topics
from .forms import TopicsForm


def topics_list(request):
    """
    Lista todos os tópicos
    """
    topics = Topics.objects.all().order_by('-id')
    context = {
        'topics': topics
    }
    return render(request, 'topics/topics_list.html', context)


def topics_detail(request, pk):
    """
    Exibe detalhes de um tópico específico
    """
    topic = get_object_or_404(Topics, pk=pk)
    context = {
        'topic': topic
    }
    return render(request, 'topics/topics_detail.html', context)


@login_required
def topics_create(request):
    """
    Cria um novo tópico
    """
    if request.method == 'POST':
        form = TopicsForm(request.POST)
        if form.is_valid():
            topic = form.save()
            messages.success(request, 'Tópico criado com sucesso!')
            return redirect('topics:topics_list')
    else:
        form = TopicsForm()

    context = {
        'form': form,
        'title': 'Novo Tópico'
    }
    return render(request, 'topics/topics_form.html', context)


@login_required
def topics_update(request, pk):
    """
    Atualiza um tópico existente
    """
    topic = get_object_or_404(Topics, pk=pk)

    if request.method == 'POST':
        form = TopicsForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tópico atualizado com sucesso!')
            return redirect('topics:topics_detail', pk=pk)
    else:
        form = TopicsForm(instance=topic)

    context = {
        'form': form,
        'topic': topic,
        'title': 'Editar Tópico'
    }
    return render(request, 'topics/topics_form.html', context)


@login_required
def topics_delete(request, pk):
    """
    Deleta um tópico
    """
    topic = get_object_or_404(Topics, pk=pk)

    if request.method == 'POST':
        topic.delete()
        messages.success(request, 'Tópico excluído com sucesso!')
        return redirect('topics:topics_list')

    context = {
        'topic': topic
    }
    return render(request, 'topics/topics_confirm_delete.html', context)
