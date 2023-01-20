from django.contrib import admin

from .models import Choice, Question, User

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'pub_date', 'was_published_recently')
    list_display_links = ('__str__', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        ("Texto pregunta", {'fields': ['question_text']}),
        ("Fecha publicación", {'fields': ['pub_date'], 
                            'classes': ['collapse']}),
        ]
    inlines = [ChoiceInline]

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Login", {'fields': ['username', 'password']}),
        ('Datos Personales', {'fields': ['firstname', 'lastname']}),
        ('Datos de Contacto', {'fields': ['email', 'address', 'phone']}),
    ]

#admin.site.register(Question, QuestionAdmin)
#admin.site.register(User, UserAdmin)