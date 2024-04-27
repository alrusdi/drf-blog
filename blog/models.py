from django.db import models


class PostStatus(models.TextChoices):
    PUBLISHED = "published", "Опубликовано"
    DRAFT = "draft", "Черновик"


class Post(models.Model):
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="posts",
    )

    title = models.CharField(
        verbose_name="Заголовок",
        max_length=1000,
    )

    text = models.TextField(
        verbose_name="Текст",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    status = models.CharField(
        max_length=50,
        choices=PostStatus.choices,
        default=PostStatus.DRAFT,
    )

    class Meta:
        verbose_name = "Запись в блоге"
        verbose_name_plural = "Записи в блоге"

    def __str__(self):
        return self.title


class CommentStatus(models.TextChoices):
    NEW = "new", "Новый"
    APPROOVED = "approoved", "Опубликован"

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name="Запись в блоге",
        on_delete=models.CASCADE,
        related_name="comments",
    )

    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="comments",
    )

    text = models.TextField(
        verbose_name="Комментарий",
    )

    status = models.CharField(
        max_length=50,
        choices=CommentStatus.choices,
        default=CommentStatus.NEW,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Комментарий к записи"
        verbose_name_plural = "Комментарии к записям"

    def __str__(self):
        return self.text[0:100]
