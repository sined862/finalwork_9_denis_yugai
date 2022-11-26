from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse, reverse_lazy 
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.shortcuts import redirect


def logout_view(request):
    logout(request)
    return redirect('login')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    