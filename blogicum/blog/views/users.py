from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

from blog.forms import UserForm
from blog.models import User
from blog.views.posts import get_posts, get_paginator


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('login')

def profile(request, username):
    """Профиль пользователя."""
    user_profile = get_object_or_404(
        User,
        username=username
    )
    posts = get_posts(author=user_profile)
    if request.user != user_profile:
        posts = get_posts(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now(),
            author=user_profile,
        )
    page_obj = get_paginator(request, posts)
    context = {
        'profile': user_profile,
        'page_obj': page_obj,
    }
    return render(request, 'blog/profile.html', context)


@login_required
def edit_profile(request):
    """Редактирование своего профиля."""
    form = UserForm(
        request.POST or None,
        instance=request.user,
        )
    if form.is_valid():
        form.save()
        return redirect('blog:profile', username=request.user.username)
    return render(request, 'blog/user.html', {'form': form})

@login_required
def my_profile(request):
    """Редирект на профиль текущего пользователя."""
    return redirect('blog:profile', username=request.user.username)