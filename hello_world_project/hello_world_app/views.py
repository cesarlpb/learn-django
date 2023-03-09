from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

# Importamos modelo Member y la función generate_slug_hash
from .models import Member
from .models import generate_slug_hash
# Importamos el formulario CreateMemberForm -> crear Member
from .forms import CreateMemberForm
from .forms import UpdateMemberForm

import datetime

# CRUD -> Member
# CREATE #
def create_member(request):
  if request.method == 'POST':
        form = CreateMemberForm(request.POST)
        if form.is_valid():
          
          # Tomamos valores del form en "member" para añadir slug_hash y slug
          member = form.save(commit=False)
          member.slug_hash = generate_slug_hash()
          # Agregamos condición para que firstname y lastname no tengan espacios
          cleaned_firstname = member.firstname.replace(" ", "").lower()
          cleaned_lastname = member.lastname.replace(" ", "").lower()
          member.slug = f"{cleaned_firstname}-{cleaned_lastname}-{member.slug_hash}"

          form.save()
          msg = f'Se ha creado el Member {member.firstname} {member.lastname}'
          return render(request, 'create_member.html', {'msg': msg})
        else: 
          error = "El formulario no es válido."
          return render(request, 'create_member.html', {'error': error})
  elif request.method == 'GET':
      form = CreateMemberForm()
      return render(request, 'create_member.html', {'form': form})

# READ #
# vista de todos los members -> read all / get all
def all_members(request):
  my_members = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'my_members': my_members,
  }
  return HttpResponse(template.render(context, request))

# vista de un member con ID -> read one / get one / get by id
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

# vista de un member con SLUG -> read one / get one / get by slug
  # issue: cuando el firstname y lastname coinciden nos arroja error -> slug + id o slug + hash
def details(request, slug):
  my_member = Member.objects.get(slug=slug)
  template = loader.get_template('member.html')
  context = {
    'my_member': my_member,
  }
  return HttpResponse(template.render(context, request))  

# UPDATE #
def update_member(request, slug):
  #member = Member.objects.get(slug=slug)
  #if member.slug == slug:
  if request.method == 'POST':
    member = Member.objects.get(slug=slug)
    form = UpdateMemberForm(request.POST, instance=member)
    if form.is_valid():
      # Actualiza los valores del member que no están vacíos del form
      for field in form.cleaned_data:
        setattr(member, field, form.cleaned_data[field])
      # Guardamos los cambios en el objeto que ya existe
      member.save()
      msg = f'Se ha actualizado el Member {member.firstname} {member.lastname}'
      return render(request, 'update_member.html', {'msg': msg})
    else: 
      error = "El formulario no es válido."
      return render(request, 'update_member.html', {'error': error})
    #else: 
    #  error = f"El member {slug} no existe."
    #  return render(request, 'update_member.html', {'error': error})
  elif request.method == 'GET':
    current_member = Member.objects.get(slug=slug)
    current_member_values = {
      "firstname" : current_member.firstname, 
      "lastname" : current_member.lastname,
      "phone" : current_member.phone,
    }
    form = UpdateMemberForm()
    return render(request, 'update_member.html', {'form': form, 'current_member_values': current_member_values, 'slug': slug})

# DELETE
def delete_member(request, slug):
  #member = Member.objects.get(slug=slug) # si el slug no existe nos arroja error
  member = Member.objects.filter(slug=slug).first()
  # if request.method == 'POST':
  if member:
    if member.slug == slug:
      # try / except
      member.delete()
      msg = f'Se ha eliminado el Member {member.slug}'
      return render(request, 'delete_member.html', {'msg': msg})
  else:
    error = f"El member {slug} no existe."
    return render(request, 'delete_member.html', {'error': error})

def home(request):
   return render(request, 'home.html')
# página de perros y gatos con modelo de Tensorflow

def modelo(request):
    return render(request, 'modelo.html')
