from django.shortcuts import get_object_or_404, render

from ..models import Category
from .posts import get_published_posts


def category_posts(request, category_slug):
    """Страница категории."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = get_published_posts().filter(category=category)
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list,
    })