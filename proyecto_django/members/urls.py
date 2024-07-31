
from django.urls import path
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
   path('', views.index, name='index'),
   path('members/', views.members, name='members'),
   path('members/details/<int:id>', views.details, name='details')
]
