from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Questions
from .forms import QuestionsForm


def questions_list(request):
    """
    Lista todas as questões
    """
    questions = Questions.objects.all().order_by('-id')
    context = {
        'questions': questions
    }
    return render(request, 'questions/questions_list.html', context)


def questions_detail(request, pk):
    """
    Exibe detalhes de uma questão específica
    """
    question = get_object_or_404(Questions, pk=pk)
    context = {
        'question': question
    }
    return render(request, 'questions/questions_detail.html', context)


@login_required
def questions_create(request):
    """
    Cria uma nova questão
    """
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            messages.success(request, 'Questão criada com sucesso!')
            return redirect('questions:questions_list')
    else:
        form = QuestionsForm()

    context = {
        'form': form,
        'title': 'Nova Questão'
    }
    return render(request, 'questions/questions_form.html', context)


@login_required
def questions_update(request, pk):
    """
    Atualiza uma questão existente
    """
    question = get_object_or_404(Questions, pk=pk)

    # Verificar se o usuário é o autor da questão
    if question.user != request.user:
        messages.error(
            request, 'Você não tem permissão para editar esta questão.')
        return redirect('questions:questions_detail', pk=pk)

    if request.method == 'POST':
        form = QuestionsForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'Questão atualizada com sucesso!')
            return redirect('questions:questions_detail', pk=pk)
    else:
        form = QuestionsForm(instance=question)

    context = {
        'form': form,
        'question': question,
        'title': 'Editar Questão'
    }
    return render(request, 'questions/questions_form.html', context)


@login_required
def questions_delete(request, pk):
    """
    Deleta uma questão
    """
    question = get_object_or_404(Questions, pk=pk)

    # Verificar se o usuário é o autor da questão
    if question.user != request.user:
        messages.error(
            request, 'Você não tem permissão para excluir esta questão.')
        return redirect('questions:questions_detail', pk=pk)

    if request.method == 'POST':
        question.delete()
        messages.success(request, 'Questão excluída com sucesso!')
        return redirect('questions:questions_list')

    context = {
        'question': question
    }
    return render(request, 'questions/questions_confirm_delete.html', context)
