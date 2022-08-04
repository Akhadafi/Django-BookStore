from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="book.all"),
    path("<int:id>", views.show, name="book.show"),
    path("review", views.review, name="book.review"),
]
