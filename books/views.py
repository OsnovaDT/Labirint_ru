from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

from books.models import (
    Book, Author, Genre,
    PublishingHouse, Series
)


# For index page
class BookListView(LoginRequiredMixin, ListView):
    template_name = 'books/index.html'
    paginate_by = 12
    context_object_name = 'books'
    queryset = Book.objects.all()


# Book detail info
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'


# Publishing house books
class PublishingHouseListView(ListView):
    template_name = 'books/publ_house_books.html'
    paginate_by = 12
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(
            publishing_house=self.kwargs['publ_house_id']
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['publ_house'] = PublishingHouse.objects.get(
            pk=self.kwargs['publ_house_id']
        )
        context['series'] = context['publ_house'].series_set.all()

        return context


# Episode books
class SeriesListView(ListView):
    template_name = 'books/episode_books.html'
    paginate_by = 12
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(
            series=self.kwargs['episode_id']
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['episode'] = Series.objects.get(
            pk=self.kwargs['episode_id']
        )

        return context


# Author books
class AuthorsListView(ListView):
    template_name = 'books/author_books.html'
    paginate_by = 12
    context_object_name = 'books'

    def get_queryset(self):

        return Book.objects.filter(
            authors=self.kwargs['author_id']
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['author'] = Author.objects.get(
            pk=self.kwargs['author_id']
        )

        return context
