from django import forms
from django import forms
from django.forms import DateField
from .models import TicketModel
from django.forms.widgets import NumberInput, DateInput


class TicketForm(forms.ModelForm):
    
    # go_date = forms.DateField()
    class Meta:
        model = TicketModel
        fields = ("name","to","go_date")
        
        
       