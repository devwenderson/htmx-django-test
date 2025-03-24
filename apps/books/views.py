from django.shortcuts import render
from apps.books.models import Book
from apps.books.form import BookForm

def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    books = Book.objects.all()
    template = 'partials/books/list.html'
    return render(request, template, {'books': books})

def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return render(request, "partials/books/detail.html", {'book': book})
    form = BookForm(instance=book)
    return render(request, "partials/books/update.html", {'form': form, 'book': book})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, "partials/books/detail.html", {'book': book})

def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        book.delete()
        books = Book.objects.all()
        return render(request, "partials/books/list.html", {'books':books})
    return render(request, "partials/books/delete.html", {'book': book})