from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def index(request):
    # Llamar a db, etc...
    print("Han solicitado index.html")
    return render(request, "index.html")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)

        # print("Me han pedido POST")
        # print(username, password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login exitoso. Bienvenido, ' + username)
            return redirect('index')
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
            return redirect('login')
        
        