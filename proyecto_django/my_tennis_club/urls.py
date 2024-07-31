"""
URL configuration for my_tennis_club project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# No tengo claro si estas importaciones van en este archivo, o en el de urls.py
# dentro de members.
from django.contrib.auth import views as auth_views
from members.views import signup_view, CustomLoginView, protected_view, signup_success_view , CustomLogoutView, sin_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('members.urls')),
    # Estas rutas lo mismo, no se si van en este archivo o en el de members
    path('signup/', signup_view, name='signup'),
    path('signup_success/', signup_success_view, name='signup_success'),  # URL para la página de éxito
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/sin_login/'), name='logout'),
    path('sin_login/', sin_login, name='sin_login'),
   # path('logged_out/', logged_out_view, name='logged_out'),
    path('protected/', protected_view, name='protected'),
]
