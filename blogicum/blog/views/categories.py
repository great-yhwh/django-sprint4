from django.shortcuts import get_object_or_404, render

from ..models import Category
from .posts import get_published_posts, get_paginator


def category_posts(request, category_slug):
    """Страница категории с пагинацией."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = get_published_posts().filter(category=category)
    page_obj = get_paginator(request, post_list)
    return render(request, 'blog/category.html', {
        'category': category,
        'page_obj': page_obj,
    })