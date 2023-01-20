from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self, request):
        result = "Esto es un string"
        return HttpResponse(result)
