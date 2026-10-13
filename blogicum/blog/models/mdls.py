from django.contrib.auth import get_user_model
from django.db import models
from .abstr import BaseModel, TitleModel

User = get_user_model()


class Location(BaseModel):
    """Модель географических точек."""

    name = models.CharField(
        max_length=256,
        verbose_name="Название места"
    )

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class Category(BaseModel, TitleModel):
    """Модель тематических категорий."""

    description = models.TextField(
        verbose_name="Описание"
    )
    slug = models.SlugField(
        max_length=256,
        unique=True,
        verbose_name="Идентификатор",
        help_text="Идентификатор страницы для URL; "
                  "разрешены символы латиницы, цифры, дефис и подчёркивание."
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Post(BaseModel, TitleModel):
    """Модель публикации блога."""

    text = models.TextField("Текст")
    pub_date = models.DateTimeField(
        "Дата и время публикации",
        help_text=(
            "Если установить дату и время в будущем — можно делать отложенные "
            "публикации."
        ),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.deletion.CASCADE,
        verbose_name="Автор публикации",
        related_name="posts",
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.deletion.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Местоположение",
        related_name="posts",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.deletion.SET_NULL,
        null=True,
        verbose_name="Категория",
        related_name="posts",
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return self.title
