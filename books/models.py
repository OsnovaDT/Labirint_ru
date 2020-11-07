from django.db import models


class Author(models.Model):
    name = models.CharField(
        'Имя',
        max_length=100,
        unique=True,
    )
    info = models.TextField(
        'Информация',
        help_text='Информация об авторе',
        null=True,
        blank=True,
    )
    image = models.ImageField(
        'Фотография',
        null=True,
        blank=True,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']


class PublishingHouse(models.Model):
    name = models.CharField(
        'Название',
        max_length=100,
        unique=True,
    )
    info = models.TextField(
        'Информация',
        help_text='Информация об издательстве',
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name='Изображение',
        null=True,
        blank=True,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'
        ordering = ['name']
