from django.urls import path

from books.views import (
    BookListView, BookDetailView, PublishingHouseListView, SeriesListView, AuthorsListView, GenreListView,
    SearchResultsView
) 

from django.views.decorators.cache import cache_page

app_name = 'books'

urlpatterns = [
    # Index
    path(
        '',
        # cache_page(60 * 30)(BookListView.as_view()),
        BookListView.as_view(),
        name='index'
    ),

    # Book detail
    path(
        'book/<int:pk>/',
        cache_page(60 * 30)(BookDetailView.as_view()),
        name='book_detail'
    ),

    # Publishing house books
    path(
        'publishing_house/<int:publ_house_id>/',
        cache_page(60 * 30)(PublishingHouseListView.as_view()),
        name='publ_house'
    ),

    # Series books
    path(
        'episode/<int:episode_id>/',
        cache_page(60 * 30)(SeriesListView.as_view()),
        name='episode'
    ),

    # Authors books
    path(
        'author/<int:author_id>/',
        cache_page(60 * 30)(AuthorsListView.as_view()),
        name='author'
    ),

    # Genre books
    path(
        'genre/<int:genre_id>/',
        cache_page(60 * 30)(GenreListView.as_view()),
        name='genre'
    ),

    # Search
    path(
        'seaarch/',
        SearchResultsView.as_view(),
        name='search_results'
    )
]
