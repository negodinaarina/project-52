from django.shortcuts import render
from django.views.generic.base import TemplateView


def home_page(request):
    return render(request, 'index.html')