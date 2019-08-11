from django.shortcuts import render
from . import models
from .forms import UserCreateForm
from django.views.generic import TemplateView, DetailView, CreateView
from django.urls import reverse_lazy

# Create your views here.

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'