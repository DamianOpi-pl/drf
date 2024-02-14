from django.urls import path

from api.views import BugFilterView

urlpatterns = [
    # path('bugs/', GetBugs.as_view()),
    path('bugs', BugFilterView.as_view()),
]
