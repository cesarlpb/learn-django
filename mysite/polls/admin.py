from django.contrib import admin

from .models import Question, User

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Texto pregunta", {'fields': ['question_text']}),
        ('Fecha publicación', {'fields': ['pub_date']}),
    ]

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Login", {'fields': ['username', 'password']}),
        ('Datos Personales', {'fields': ['firstname', 'lastname']}),
        ('Datos de Contacto', {'fields': ['email', 'address', 'phone']}),
    ]
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(User, UserAdmin)