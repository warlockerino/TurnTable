from django.forms import ModelForm
from .models import Table

class TableForm(ModelForm):

    class Meta:
        model = Table
        fields = (
            'name',
            'description', 
            'city',
        )
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(TableForm, self).__init__(*args, **kwargs)

    
    def save(self, commit=True):
        data = self.cleaned_data
        Table.description = data['description']
        Table.city = self.cleaned_data['city']
        Table.people = self.cleaned_data['people']
        return Table

        
