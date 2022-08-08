from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    return render(request, "infos/home.html")

def me(request):
    return render(request, "infos/me.html")

def contact(request):
    return render(request, "infos/contact.html")
    