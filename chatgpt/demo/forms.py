from django import forms
from .models import ChatGptQuery

class NewQueryForm(forms.ModelForm):
    class Meta:
        model = ChatGptQuery
        fields = ['prompt']

    def __init__(self, *args, **kwargs):
        super(NewQueryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'