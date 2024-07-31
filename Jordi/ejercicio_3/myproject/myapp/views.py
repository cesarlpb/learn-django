import requests
import json
from django.http import JsonResponse

def fetch_data(request):
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        formatted_data = [{'id': item['id'], 'title': item['title']} for item in data]
        
        # Formatear los datos con indentación de 4 espacios
        formatted_json = json.dumps({'data': formatted_data}, indent=4)
        
        return JsonResponse(json.loads(formatted_json), json_dumps_params={'indent': 4})
    else:
        return JsonResponse({'error': 'Unable to fetch data from external API'}, status=500)
