from django import forms
from .models import Item 

class ItemForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'placeholder':'Título'}))
    description = forms.CharField(label='',
                                  required=False,
                                  widget=forms.Textarea(attrs={'placeholder':'Descripción'}))
    class Meta:
        model = Item 
        fields = [
            'title',
            'description',
        ]

