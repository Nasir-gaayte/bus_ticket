from django import forms
from django import forms
from django.forms import DateField
from .models import TicketModel
from django.forms.widgets import NumberInput, DateInput,SelectDateWidget


class TicketForm(forms.ModelForm):
    
    go_date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = TicketModel
        fields = ("name","email","phone", "to","go_date")
        
        
       