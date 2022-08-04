from django.shortcuts import redirect, render, get_object_or_404
from .models import Book, Review
from django.views.generic import ListView, DetailView


class BookListView(ListView):
    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book
    # reviews = Review.objects.filter(book_id=id).order_by("-created_at")


def review(request, id):
    body = request.POST["review"]
    newReview = Review(body=body, book_id=id)
    newReview.save()
    return redirect("/book")
