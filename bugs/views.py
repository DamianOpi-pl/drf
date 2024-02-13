from django.views import View
from django.shortcuts import render


class BugPageView(View):
    template_name = "bugs.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)
