from django.urls import path

from bugs.views import BugPageView

urlpatterns = [
    path('', BugPageView.as_view()),
]
