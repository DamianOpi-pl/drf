from django.contrib import admin
from django.urls import path
from books.views import BooksView, BooksUpdateView,SingleBookView

urlpatterns = [
    path('', BooksView.as_view()),
    path('<int:pk>', SingleBookView.as_view()),
    path('db', BooksUpdateView.as_view()),
]
