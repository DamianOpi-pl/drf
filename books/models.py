from django.db import models


class BooksSearch(models.Model):
    search_phrase = models.CharField(max_length=100, null=False)
    response_data = models.JSONField()


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.TextField(null=True)
    published_date = models.CharField(max_length=10, null=True)
    categories = models.TextField(null=True)
    average_rating = models.IntegerField(null=True)
    ratings_count = models.IntegerField(null=True)
    thumbnail = models.CharField(max_length=200, null=True)
