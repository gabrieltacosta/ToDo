from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def sobre(request):
    return render(request, "about/about.html")
