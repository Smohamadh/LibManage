from django.urls import path
from LMapp.views import GetAllAuthors, GetAllPublishers,  PostModelBook,\
    SearchBooksFromAuthor, SearchBooksFromPublisher, GetAllBooks

urlpatterns = [
    path('get_all_author', GetAllAuthors.as_view()),
    path('get_all_publisher', GetAllPublishers.as_view()),
    path('get_all_book', GetAllBooks.as_view()),
    path('post_book/', PostModelBook.as_view()),
    path('search_books_author/', SearchBooksFromAuthor.as_view()),
    path('search_books_publisher/', SearchBooksFromPublisher.as_view()),
]
