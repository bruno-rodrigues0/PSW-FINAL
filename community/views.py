from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Community
from .forms import CommunityForm


def community_list(request):
    """
    Lista todas as comunidades
    """
    communities = Community.objects.all().order_by('-id')
    context = {
        'communities': communities
    }
    return render(request, 'pages/list.html', context)


def community_detail(request, pk):
    """
    Exibe detalhes de uma comunidade específica
    """
    community = get_object_or_404(Community, pk=pk)
    context = {
        'community': community
    }
    return render(request, 'pages/detail.html', context)


# @login_required
def community_create(request):
    """
    Cria uma nova comunidade
    """
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = form.save(commit=False)
            community.owner = request.user
            community.save()
            messages.success(request, 'Comunidade criada com sucesso!')
            return redirect('community:community_list')
    else:
        form = CommunityForm()

    context = {
        'form': form,
        'title': 'Nova Comunidade'
    }
    return render(request, 'pages/form.html', context)


# @login_required
def community_update(request, pk):
    """
    Atualiza uma comunidade existente
    """
    community = get_object_or_404(Community, pk=pk)

    # Verificar se o usuário é o dono da comunidade
    if community.owner != request.user:
        messages.error(
            request, 'Você não tem permissão para editar esta comunidade.')
        return redirect('community:community_detail', pk=pk)

    if request.method == 'POST':
        form = CommunityForm(request.POST, instance=community)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comunidade atualizada com sucesso!')
            return redirect('community:community_detail', pk=pk)
    else:
        form = CommunityForm(instance=community)

    context = {
        'form': form,
        'community': community,
        'title': 'Editar Comunidade'
    }
    return render(request, 'pages/form.html', context)


# @login_required
def community_delete(request, pk):
    """
    Deleta uma comunidade
    """
    community = get_object_or_404(Community, pk=pk)

    # Verificar se o usuário é o dono da comunidade
    if community.owner != request.user:
        messages.error(
            request, 'Você não tem permissão para excluir esta comunidade.')
        return redirect('community:community_detail', pk=pk)

    if request.method == 'POST':
        community.delete()
        messages.success(request, 'Comunidade excluída com sucesso!')
        return redirect('community:community_list')

    context = {
        'community': community
    }
    return render(request, 'community/delete.html', context)
