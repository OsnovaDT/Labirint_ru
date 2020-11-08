from django.urls import path

from books.views import (
    BookListView, BookDetailView, PublishingHouseListView, SeriesListView,
    AuthorsListView, GenreListView
) 


app_name = 'books'

urlpatterns = [
    # Index
    path('', BookListView.as_view(), name='index'),

    # Book detail
    path(
        'book/<int:pk>/',
        BookDetailView.as_view(),
        name='book_detail'
    ),

    # Publishing house books
    path(
        'publishing_house/<int:publ_house_id>/',
        PublishingHouseListView.as_view(),
        name='publ_house'
    ),

    # Series books
    path(
        'episode/<int:episode_id>/',
        SeriesListView.as_view(),
        name='episode'
    ),

    # Authors books
    path(
        'author/<int:author_id>/',
        AuthorsListView.as_view(),
        name='author'
    ),

    # Genre books
    path(
        'genre/<int:genre_id>/',
        GenreListView.as_view(),
        name='genre'
    ),
]
