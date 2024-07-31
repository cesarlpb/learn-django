"""
Crear un sistema de autenticación que permita a los usuarios registrarse, iniciar sesión y acceder a una página protegida. Utilizar el sistema de autenticación integrado de Django (django.contrib.auth). Crear vistas para registro (SignupView), inicio de sesión (LoginView) y cierre de sesión (LogoutView). Usar decoradores como @login_required para proteger las vistas. Configurar las URLs correspondientes en urls.py.
"""

### Paso 1: Configurar el proyecto y la aplicación

django-admin startproject myproject
cd myproject
django-admin startapp myapp

### Paso 2: Configurar el archivo `settings.py`

INSTALLED_APPS = [
    ...
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp', 
]

LOGIN_REDIRECT_URL = 'protected'  # Redirigir después del login
LOGOUT_REDIRECT_URL = 'login'     # Redirigir después del logout

### Paso 3: Crear formularios de registro en `myapp/forms.py`:

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

### Paso 4: Crear vistas de registro, inicio de sesión y cierre de sesión. En `myapp/views.py`:

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import View
from .forms import SignUpForm

def index(request):
    return render(request, 'index.html')

class SignUpView(View):
    form_class = SignUpForm
    template_name = 'signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Cargar el perfil del usuario creado
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('protected')
        return render(request, self.template_name, {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    template_name = 'logged_out.html'

@login_required
def protected_view(request):
    return render(request, 'protected.html')

### Paso 5: Configurar las URLs. En `myproject/urls.py`:

from django.contrib import admin
from django.urls import path, include
from myapp.views import SignUpView, CustomLoginView, CustomLogoutView, protected_view, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('protected/', protected_view, name='protected'),
    path('', index, name='index'),
]

### Paso 6: Crear htmls, en `myapp/templates`:

#### `index.html`
<!DOCTYPE html>
<html>
<head>
    <title>Main Page</title>
</head>
<body>
    <h1>Welcome to the Main User Page</h1>
    <a href="{% url 'signup' %}">User signup</a>
    <br><br>
    <a href="{% url 'login' %}">User login</a>
</body>
</html>

#### `signup.html`

<!DOCTYPE html>
<html>
<head>
    <title>Sign Up</title>
</head>
<body>
    <h2>Sign Up</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Sign Up</button>
    </form>
    <br>
    <a href="{% url 'index' %}">Main Page</a>
</body>
</html>

#### `login.html`

<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
    </form>
    <br>
    <a href="{% url 'index' %}">Main Page</a>
</body>
</html>

#### `protected.html`

<!DOCTYPE html>
<html>
<head>
    <title>Protected Page</title>
</head>
<body>
    <h2>Protected Page</h2>
    <p>Welcome, {{ user.username }}!</p>
    <a href="{% url 'logout' %}">Logout</a>
</body>
</html>

#### `logged_out.html`

<!DOCTYPE html>
<html>
<head>
    <title>Logged Out</title>
</head>
<body>
    <h2>You have been logged out</h2>
    <a href="{% url 'login' %}">Login again</a>
</body>
</html>

### Paso 7: Migrar la base de datos y ejecutar el servidor:

python manage.py migrate

python manage.py runserver

### Paso 8: Prueba

Acceder a la ruta:

http://127.0.0.1:8000