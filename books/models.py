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


# Publishing house series
class Series(models.Model):
    name = models.CharField(
        'Название',
        max_length=100,
        unique=True,
    )
    info = models.TextField(
        'Информация',
        help_text='Информация о серии',
        null=True,
        blank=True,
    )
    publishing_house = models.ForeignKey(
        'PublishingHouse',
        on_delete=models.CASCADE,
        verbose_name='Издательство'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'
        ordering = ['name']


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название',
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']
