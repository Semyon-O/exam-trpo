# accounts/views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from .models import Order, Equipment


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # замените 'home' на ваше имя URL
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # замените 'login' на ваше имя URL для страницы авторизации
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required()
def home_view(request):
    orders = Order.objects.filter(client=request.user.client)  # Получаем заявки только для текущего пользователя
    return render(request, 'home.html', {'orders': orders})


@login_required()
def equipment_view(request):
    equipment = Equipment.objects.filter(client=request.user.client)
    return render(request, 'equipment.html', context={'equipment': equipment})