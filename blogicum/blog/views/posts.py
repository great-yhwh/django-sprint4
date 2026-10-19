from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from ..models import Post


def get_published_posts():
    """
    Возвращает список объектов отфильтрованных публикаций.

    Критерии отбора публикаций:
        1. Дата публикации — не позже текущего времени.
        2. Флаг публикации самого поста равен True.
        3. Флаг публикации категории, к которой принадлежит
           пост, равен True.
    """
    return (
        Post.objects
        .select_related('author', 'category', 'location')
        .filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True,
        )
    )


def index(request):
    """Главная страница: 5 последних публикаций."""
    post_list = get_published_posts()[:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    """Страница отдельной публикации."""
    post = get_object_or_404(get_published_posts(), pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})