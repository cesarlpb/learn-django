from django.shortcuts import render
# from django.http import HttpResponse
from .models import Member

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

def members(request):
    mymembers = Member.objects.all()
    context = {
        'mymembers': mymembers,
    }
    return render(request, "all_members.html", context)

def index(request):
    return render(request, "index.html")

def details(request, id):
    mymember = Member.objects.get(id=id)
    context = {
        'mymember': mymember,
    }
    return render(request, "details.html", context)


def signup_success_view(request):
    return render(request, 'registration/signup_success.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('signup_success')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'

def logged_out_view(request):
    logout(request)
    return redirect('test')
        
def sin_login(request):
    return render(request, 'registration/sin_login.html')

@login_required
def protected_view(request):
    return render(request, 'protected.html')