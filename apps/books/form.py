from django.forms import ModelForm
from apps.books.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price']