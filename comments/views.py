from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Comment
from .forms import CommentForm


class CommentListView(ListView):
    model = Comment
    template_name = 'comments/comment_list.html'
    context_object_name = 'comments'


def comment_list(request):
    """
    Lista todos os comentários
    """
    comments = Comment.objects.all().order_by('-created_at')
    context = {
        'comments': comments
    }
    return render(request, 'comments/comment_list.html', context)


class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comments/comment_detail.html'
    context_object_name = 'comment'


def comment_detail(request, pk):
    """
    Exibe detalhes de um comentário específico
    """
    comment = get_object_or_404(Comment, pk=pk)
    context = {
        'comment': comment
    }
    return render(request, 'comments/comment_detail.html', context)


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/comment_form.html'
    success_url = reverse_lazy('comment_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def comment_create(request):
    """
    Cria um novo comentário
    """
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comentário criado com sucesso!')
            return redirect('comment_list')
    else:
        form = CommentForm()

    context = {
        'form': form,
        'title': 'Novo Comentário'
    }
    return render(request, 'comments/comment_form.html', context)


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/comment_form.html'
    success_url = reverse_lazy('comment_list')


def comment_update(request, pk):
    """
    Atualiza um comentário existente
    """
    comment = get_object_or_404(Comment, pk=pk)

    # Verificar se o usuário é o autor do comentário
    if comment.user != request.user:
        messages.error(
            request, 'Você não tem permissão para editar este comentário.')
        return redirect('comment_detail', pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comentário atualizado com sucesso!')
            return redirect('comment_detail', pk=pk)
    else:
        form = CommentForm(instance=comment)

    context = {
        'form': form,
        'comment': comment,
        'title': 'Editar Comentário'
    }
    return render(request, 'comments/comment_form.html', context)


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comments/comment_confirm_delete.html'
    success_url = reverse_lazy('comment_list')


def comment_delete(request, pk):
    """
    Deleta um comentário
    """
    comment = get_object_or_404(Comment, pk=pk)

    # Verificar se o usuário é o autor do comentário
    if comment.user != request.user:
        messages.error(
            request, 'Você não tem permissão para excluir este comentário.')
        return redirect('comment_detail', pk=pk)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comentário excluído com sucesso!')
        return redirect('comment_list')

    context = {
        'comment': comment
    }
    return render(request, 'comments/comment_confirm_delete.html', context)
