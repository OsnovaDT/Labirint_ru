from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.db.models import Q

from books.models import (
    Book, Author, Genre,
    PublishingHouse, Series
)
from books.forms import RegistrationForm


# For index page
class BookListView(LoginRequiredMixin, ListView):
    template_name = 'books/index.html'
    paginate_by = 12
    context_object_name = 'books'
    queryset = Book.objects.prefetch_related(
        'publishing_house', 'series', 'authors'
    )


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
        ).prefetch_related(
            'publishing_house', 'series', 'authors'
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['publ_house'] = PublishingHouse.objects.get(
            pk=self.kwargs['publ_house_id']
        )
        context['series'] = context['publ_house'].series.all()

        return context


# Episode books
class SeriesListView(ListView):
    template_name = 'books/episode_books.html'
    paginate_by = 12
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(
            series=self.kwargs['episode_id']
        ).prefetch_related(
            'publishing_house', 'series', 'authors'
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
        ).prefetch_related(
            'publishing_house', 'series', 'authors'
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['author'] = Author.objects.get(
            pk=self.kwargs['author_id']
        )

        return context


# Genre books
class GenreListView(ListView):
    template_name = 'books/genre_books.html'
    paginate_by = 12
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(
            genres=self.kwargs['genre_id']
        ).prefetch_related(
            'publishing_house', 'series', 'authors'
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['genre'] = Genre.objects.get(
            pk=self.kwargs['genre_id']
        )

        return context


class SignUpView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/sign_up.html'
    success_url = reverse_lazy('login')


class SearchResultsView(ListView):
    model = Book
    template_name = 'books/search_results.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q')
        
        return Book.objects.filter(
            Q(title__icontains=query) | Q(authors__name__icontains=query)
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search_field'] = self.request.GET.get('q')

        return context
