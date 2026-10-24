from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone

from ..forms import PostForm, CommentForm
from ..models import Post, Comment

PAGINATOR = 10

def get_published_posts():
    return (
        Post.objects
        .select_related('author', 'category', 'location')
        .annotate(comment_count=Count('comments'))
        .filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True,
        )
        .order_by('-pub_date')
    )


def index(request):
    """Главная страница с пагинацией."""
    post_list = get_published_posts()
    page_obj = get_paginator(request, post_list)
    return render(request, 'blog/index.html', {'page_obj': page_obj})


def post_detail(request, post_id):
    """Страница отдельной публикации."""
    post = get_object_or_404(
        Post.objects.select_related('author', 'category', 'location'),
        pk=post_id,
    )
    if not (
            post.is_published
            and post.category.is_published
            and post.pub_date <= timezone.now()
    ):
        if not request.user.is_authenticated or request.user != post.author:
            from django.http import Http404
            raise Http404

    comments = post.comments.select_related('author').order_by('created_at')
    form = CommentForm()
    return render(request, 'blog/detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })


@login_required
def create_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('blog:profile', username=request.user.username)
    return render(request, 'blog/create.html', {'form': form})

def edit_post(request, post_id):
    """Редактирование публикации."""
    post = get_object_or_404(Post, pk=post_id)
    if not request.user.is_authenticated or request.user != post.author:
        return redirect('blog:post_detail', post_id=post.id)
    form = PostForm(
        request.POST or None,
        request.FILES or None,
        instance=post,
        )
    if form.is_valid():
        form.save()
        return redirect('blog:post_detail', post_id=post.id)
    return render(request, 'blog/create.html', {'form': form})


@login_required
def delete_post(request, post_id):
    """Удаление публикации (только автор)."""
    post = get_object_or_404(Post, pk=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:profile', username=request.user.username)
    return render(request, 'blog/detail.html', {'post': post})


@login_required
def add_comment(request, post_id):
    """Добавление комментария к посту."""
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        return redirect('blog:post_detail', post_id=post.id)
    return redirect('blog:post_detail', post_id=post.id)


@login_required
def edit_comment(request, post_id, comment_id):
    """Редактирование комментария (только автор комментария)."""
    comment = get_object_or_404(
        Comment,
        pk=comment_id,
        post_id=post_id,
        author=request.user,
    )
    form = CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        form.save()
        return redirect('blog:post_detail', post_id=post_id)
    return render(request, 'blog/comment.html', {
        'form': form,
        'comment': comment,
    })


@login_required
def delete_comment(request, post_id, comment_id):
    """Удаление комментария (только автор комментария)."""
    comment = get_object_or_404(
        Comment,
        pk=comment_id,
        post_id=post_id,
        author=request.user,
    )
    if request.method == 'POST':
        comment.delete()
        return redirect('blog:post_detail', post_id=post_id)
    return render(request, 'blog/comment.html', {'comment': comment})


def get_posts(**kwargs):
    """Отфильтрованное получение постов."""
    return (
        Post.objects
        .select_related('category', 'location', 'author')
        .annotate(comment_count=Count('comments'))
        .filter(**kwargs)
        .order_by('-pub_date')
    )


def get_paginator(request, queryset, number_of_pages=PAGINATOR):
    """Пагинация."""
    paginator = Paginator(queryset, number_of_pages)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)