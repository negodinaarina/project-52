from django.shortcuts import render
from django.views.generic.base import TemplateView


def home_page(request):
    return render(request, 'index.html')


def users_page(request):
    pass


def login_page(request):
    pass


def register_page(request):
    pass