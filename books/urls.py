from django.urls import path

from books.views import BookListView


app_name = 'books'

urlpatterns = [
    # Index
    path('', BookListView.as_view(), name='index')
]
