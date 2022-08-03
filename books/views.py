from django.shortcuts import render
import json

booksData = open("C:/Users/HP/Documents/GitHub/Django-BookStore/books.json").read()

data = json.loads(booksData)


def index(request):
    context = {
        "books": data,
    }
    return render(request, "books/index.html", context)
