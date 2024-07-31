from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
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

class CustomLogoutView(View):
    template_name = 'logged_out.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

@login_required
def protected_view(request):
    return render(request, 'protected.html')

