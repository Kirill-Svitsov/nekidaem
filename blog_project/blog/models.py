from django.db import models

from users.models import User


class Blog(models.Model):
    """Модель блога"""
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Блог'
    )

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ('id',)

    def __str__(self):
        return f'Блог {self.user.username}'


class Post(models.Model):
    """Модель поста"""
    blog = models.ForeignKey(
        to=Blog,
        on_delete=models.CASCADE,
        related_name='post',
        verbose_name='Пост'
    )
    title = models.CharField(max_length=140, verbose_name='Заголовок поста')
    text = models.CharField(max_length=255, verbose_name='Текст поста')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    read = models.BooleanField(default=False, verbose_name='Прочитано')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-created_at',)

    def __str__(self):
        return f'Post {self.pk}'


class Subscription(models.Model):
    """Модель подписки на блог"""
    subscriber = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name='Подписчик'
    )
    blog = models.ForeignKey(
        to=Blog,
        on_delete=models.CASCADE,
        related_name='blog',
        verbose_name='Блог, на который подписан'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        unique_together = ('subscriber', 'blog')

    def __str__(self):
        return f'{self.subscriber.username} подписан на блог {self.blog.user.username}'
