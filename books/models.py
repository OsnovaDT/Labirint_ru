from django.db import models


COVER_TYPES = (
    ('solid', '7Б - твердая (плотная бумага или картон)'),
    ('soft', 'мягкий переплет (крепление скрепкой или клеем)'),
    ('with_flaps', 'Обл. с клапанами'),
)
ILLUSTRATIONS_INFO = (
    ('bw', 'Черно-белые'),
    ('color', 'Цветные'),
    ('none', 'Без иллюстраций'),
)


class Author(models.Model):
    name = models.CharField(
        'Имя',
        max_length=100,
        unique=True,
    )
    full_name = models.CharField(
        'Полное имя',
        max_length=100,
        unique=True,
        default='aaaa'
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
    publishing_house = models.ForeignKey(
        'PublishingHouse',
        on_delete=models.CASCADE,
        verbose_name='Издательство',
        related_name='series'
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


class Book(models.Model):
    title = models.CharField(
        'Название',
        max_length=255
    )
    authors = models.ManyToManyField(
        'Author',
        verbose_name='Авторы',
    )
    publishing_house = models.ForeignKey(
        'PublishingHouse',
        on_delete=models.CASCADE,
        verbose_name='Издательство',
    )
    series = models.ForeignKey(
        'Series',
        on_delete=models.CASCADE,
        verbose_name='Серия',
        null=True,
        blank=True,
    )

    price = models.PositiveIntegerField('Цена')

    genres = models.ManyToManyField(
        'Genre',
        verbose_name='Жанр',
        blank=True
    )

    ID = models.PositiveIntegerField('ID')

    ISBN = models.CharField('ISBN', max_length=30)

    pages_amount = models.PositiveIntegerField(
        'Количество страниц'
    )

    weight = models.PositiveIntegerField('Масса')

    sizes = models.CharField('Размеры', max_length=20)
    
    cover_type = models.CharField(
        'Тип обложки',
        max_length=50,
        choices=COVER_TYPES,
        default='solid'
    )
    illustrations_info = models.CharField(
        'Информация об иллюстрации',
        max_length=50,
        choices=ILLUSTRATIONS_INFO,
        default='bw'
    )
    annotation = models.TextField(
        'Аннотация',
        null=True,
        blank=True
    )
    published_date = models.DateField(
        'Дата публикации',
        auto_now_add=True
    )
    image = models.ImageField(
        'Изображение',
    )

    def get_authors(self):
        return '\n'.join(
            [author.name for author in self.authors.all()]
        )

    def get_genres(self):
        return '\n'.join(
            [genre.name for genre in self.genres.all()]
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['published_date', 'title']
