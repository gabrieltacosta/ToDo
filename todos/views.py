from django.shortcuts import render
from django.views.generic import ListView
from .models import Todo


# Create your views here.
class TodolListView(ListView):
    model = Todo

