import json
from django.http import JsonResponse
from .models import User

def user_list(request):
    users = User.objects.all().values('username', 'email', 'first_name', 'last_name')
    users_list = list(users)
    
    # Formatear los datos con indentación de 4 espacios
    formatted_json = json.dumps(users_list, indent=4)
    
    return JsonResponse(json.loads(formatted_json), safe=False, json_dumps_params={'indent': 4})
