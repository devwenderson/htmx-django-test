from django.urls import path
from apps.books.views import index, book_create, book_update, book_detail, book_delete

urlpatterns = [
    path('', index, name='index'),
    # Used at HTMX
    path("livros/criar/", book_create, name="book-create"),
    path("livros/editar/<int:pk>", book_update, name="book-update"),
    path("livros/<int:pk>", book_detail, name="book-detail"),
    path("livros/deletar/<int:pk>", book_delete, name="book-delete"),
]