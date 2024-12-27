from django.views.generic import ListView , CreateView, UpdateView , TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CustomUserChangeForm , CustomUserCreationForm
from django.contrib.auth import logout

# Create your views here.
#Login
class UserLoginView(LoginView):
    template_name = "app_usuarios/login.html"
#Vista panel
class PanelView(LoginRequiredMixin, TemplateView):
    template_name = "app_usuarios/panel.html"

#listar los usuarios
class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "app_usuarios/usuario_list.html"
    context_object_name = "users"

#crear usuario
class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "app_usuarios/usuario_create.html"
    success_url = reverse_lazy("app_usuarios:usuario_list")

#Cambios en el usuario
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = "app_usuarios/usuario_edit.html"
    success_url = reverse_lazy("app_usuarios:usuario_list")

#definicion para el logout
def logout_view(request):
    logout(request)
    return redirect('index:index')  # Cambia 'index:index' por la URL a la que quieres redirigir



