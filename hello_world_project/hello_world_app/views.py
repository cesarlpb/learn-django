from django.template import loader
from django.http import HttpResponse
from .models import Member
import datetime

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
  
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('testing.html')
  members = Member.objects.all().values()
  context = {
    'frutas': ['Apple', 'Banana', 'Cherry', 'Pineapple'],
    'members': members,
    'heading_no_esc' : "<h1>Heading1</h1>",
    'heading_esc' : "&lt;h1&gt;Heading1&lt;/h1&gt;",
    'html' : """<div>
                  <p>
                    <ul>
                      <li>Algo</li>
                    </ul>
                  </p>
                </div>
              """,
    'colors': ['Red', None, 'Blue', '', 'Yellow'],
    'meses' : [ "Enero" , "Febrero" , "Marzo" , "Abril" , "Mayo" , "Junio" , "Julio" , "Agosto" , "Septiembre" , "Octubre" , "Noviembre" , "Diciembre"],
    'texto': """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Esto es un texto con múltiples líneas.

    Salto de línea doble.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.""",
    "phone" : "123-Django",
    "lista" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "lista_2" : [1, 2, 3, 5, 5, 5, 5, 8, 9, 10],
    "texto_2" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 
    "texto_3" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
    "total_price" : 100,
    "total_price_2" : False,
    "total_price_3" : None,
    'date_1': datetime.datetime(2000, 1, 1),   
    'date_2': datetime.datetime(2023, 1, 1), 
    'date_3': datetime.datetime(2050, 1, 1),
  }
  return HttpResponse(template.render(context, request))