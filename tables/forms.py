from django import forms
from .models import Table

class TableForm(forms.ModelForm):

    class Meta:
        model = Table
        fields = (
            'owner', 
            'description', 
            'city',
            'created',
            'updated',
            'people',
        )

    
    def save(self, commit=True):
        Table.owner = self.cleaned_data['owner']
        Table.description = self.cleaned_data['description']
        Table.city = self.cleaned_data['city']
        Table.people = self.cleaned_data['people']
        return Table
