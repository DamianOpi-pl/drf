from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls")),
    path("bugs/", include("bugs.urls")),
    path("books/", include("books.urls")),
]
