from django import forms
from .models import Member

class CreateMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'phone']

    def __init__(self, *args, **kwargs):
        super(CreateMemberForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'

class UpdateMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'phone']

    def __init__(self, *args, **kwargs):
        super(UpdateMemberForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'