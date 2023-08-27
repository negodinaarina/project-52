from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .forms import UserForm
from django.contrib import messages
from .models import User


def home_page(request):
    return render(request, 'index.html')


def users_page(request):
    users = User.objects.all()
    return render(request, 'users.html', context={'users': users})


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        user = User.objects.filter(email=form.data['email'])
        if user.count():
            messages.add_message(request, messages.ERROR, 'Пользователь уже существует!')
        else:
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'Регистрация прошла успешно!')
                return redirect('users')
            else:
                messages.add_message(request, messages.INFO, 'Ошибка заполнения формы')
    form = UserForm()
    context = {'form': form}
    return render(request, 'create_user.html', context)


def update_user(request, id):
    pass


def delete_user(request, id):
    pass


def login_page(request):
    pass

