from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "homepage.html", context=None)


class AboutMePageView(TemplateView):
    template_name = 'aboutme.html'
    # def get(self, request, **kwargs):
    # return render(request, "aboutme.html", context=None)


class ContactPageView(TemplateView):
    template_name = 'contact.html'
    # def get(self, request, **kwargs):
    # return render(request, "homepage.html", context=None)
