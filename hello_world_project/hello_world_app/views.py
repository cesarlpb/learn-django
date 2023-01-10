from django.template import loader
from django.http import HttpResponse

def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())
  