from django.db import models


class BaseModel(models.Model):
    is_published = models.BooleanField(
        "Опубликовано",
        default=True,
        help_text="Снимите галочку, чтобы скрыть публикацию."
    )
    created_at = models.DateTimeField(
        'Добавлено',
        auto_now_add=True
    )

    class Meta:
        abstract = True


class TitleModel(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name="Заголовок"
    )

    class Meta:
        abstract = True
