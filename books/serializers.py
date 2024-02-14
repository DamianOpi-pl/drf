from rest_framework import serializers

from books.models import Book


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title","authors","published_date","categories","average_rating","ratings_count","thumbnail"]
