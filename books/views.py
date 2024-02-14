from django_filters import rest_framework as filters
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from books.data_downloader import DataDownloader
from books.models import Book
from books.serializers import BooksSerializer


class BookFilter(filters.FilterSet):
    author = filters.CharFilter(field_name="authors", lookup_expr='icontains')
    published_date = filters.CharFilter(field_name="published_date", lookup_expr='icontains')

    sort = filters.OrderingFilter(
        fields=(
            ('published_date', 'published_date')))

    class Meta:
        model = Book
        fields = ['authors', 'published_date']


class SingleBookView(generics.RetrieveAPIView):
    serializer_class = BooksSerializer
    queryset = Book


class BooksView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter


class BooksUpdateView(APIView):

    def post(self, *args, **kwargs):
        search_phrase = self.request.query_params.get('q', None)

        if search_phrase:
            search_results = DataDownloader.fetch(search_phrase)
            for item in search_results:
                title = item["volumeInfo"]["title"]
                if "authors" in item["volumeInfo"]:
                    authors = item["volumeInfo"]["authors"]
                else:
                    authors = None
                if "publishedDate" in item["volumeInfo"]:
                    published_date = item["volumeInfo"]["publishedDate"]
                else:
                    published_date = None
                if "categories" in item["volumeInfo"]:
                    categories = item["volumeInfo"]["categories"]
                else:
                    categories = None
                if "averageRating" in item["volumeInfo"]:
                    average_rating = item["volumeInfo"]["averageRating"]
                else:
                    average_rating = None
                if "ratingsCount" in item["volumeInfo"]:
                    ratings_count = item["volumeInfo"]["ratingsCount"]
                else:
                    ratings_count = None
                if "imageLinks" in item["volumeInfo"]:
                    thumbnail = item["volumeInfo"]["imageLinks"]["thumbnail"]
                else:
                    thumbnail = None
                Book.objects.update_or_create(title=title,
                                              authors=authors,
                                              published_date=published_date,
                                              categories=categories,
                                              average_rating=average_rating,
                                              ratings_count=ratings_count,
                                              thumbnail=thumbnail)
            return Response(status=status.HTTP_201_CREATED)
        else:
            raise NotFound()
