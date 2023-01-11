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

def member(request, member_id):
    if not isinstance(member_id, int):
        return HttpResponse(f"Member id {member_id} no es válido. El id debe ser un entero positivo.")
    elif member_id is None or member_id < 1:
        return HttpResponse(f"Member id {member_id} no es válido. El id debe ser un entero positivo.")
    
    try:
        my_member = Member.objects.get(pk=member_id)
        template = loader.get_template('member.html')
        context = {
        'my_member': my_member,
        }
        return HttpResponse(template.render(context, request))
    except Member.DoesNotExist as err:
        return HttpResponse(f"Member with id {member_id} does not exist. Error: {err}")
  
  