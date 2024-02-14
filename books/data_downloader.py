import requests
from books.models import BooksSearch


class DataDownloader:
    request_url = 'https://www.googleapis.com/books/v1/volumes?q='

    @classmethod
    def fetch(cls, q):
        response = requests.get(cls.request_url + q)
        if response.status_code == 200:
            return response.json()["items"]
        return None
