from django.shortcuts import render

def index(request):
    # Llamar a db, etc...
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")