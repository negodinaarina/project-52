from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import User


def home_page(request):
    return render(request, 'index.html')


def users_page(request):
    users = User.objects.all()
    return render(request, 'users.html', context={'users': users})


def create_user(request):
    pass


def update_user(request):
    pass


def delete_user(request):
    pass


def login_page(request):
    pass

