from django.shortcuts import render

def index(request):
    # Llamar a db, etc...
    return render(request, "index.html")

def login(request):
    if request.method == "GET":
        print("Me han pedido GET")
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("Me han pedido POST")
        print(username, password)
        mensaje = "Login recibido. Hola " + username  + "!"
        return render(request, "index.html", context={"mensaje": mensaje})