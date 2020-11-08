from django.views.generic.list import ListView

from books.models import (
    Book, Author, Genre,
    PublishingHouse, Series
)


# For index page
class BookListView(ListView):
    template_name = 'books/index.html'
    paginate_by = 12
    context_object_name = 'books'
    queryset = Book.objects.all()
