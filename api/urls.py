from django.contrib import admin
from django.urls import path
from api.views import GetBugs,BugFilterView

urlpatterns = [
    # path('bugs/', GetBugs.as_view()),
    path('bugs', BugFilterView.as_view()),
]
