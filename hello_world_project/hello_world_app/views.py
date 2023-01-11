from django.template import loader
from django.http import HttpResponse
from .models import Member

def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())

def all_members(request):
  my_members = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'my_members': my_members,
  }
  return HttpResponse(template.render(context, request))