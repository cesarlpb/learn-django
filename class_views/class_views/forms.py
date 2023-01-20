from django import forms
from .models import Animal

class CreateAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'species', 'sound']

    def __init__(self, *args, **kwargs):
        super(CreateAnimalForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'

"""
class UpdateAnimalForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'phone']

    def __init__(self, *args, **kwargs):
        super(UpdateMemberForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'
"""