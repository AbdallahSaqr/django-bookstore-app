from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = "bookstore/book_list.html"
    context_object_name = "books"

class BookDetailView(DetailView):
    model = Book
    template_name = "bookstore/book_detail.html"

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'published_date'] 
    template_name = "bookstore/book_form.html"
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'published_date']  
    template_name = "bookstore/book_form.html"
    success_url = reverse_lazy('book-list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = "bookstore/book_confirm_delete.html"
    success_url = reverse_lazy('book-list')
