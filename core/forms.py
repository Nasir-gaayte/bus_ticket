from django import forms
from django import forms
from .models import TicketModel


class TicketForm(forms.ModelForm):
    class Meta:
        model = TicketModel
        fields = ("name","to")