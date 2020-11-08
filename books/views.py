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
