from contextlib import nullcontext
from email.policy import default
from re import T
from django.db import models
from django.forms.widgets import NumberInput
import datetime
# Create your models here.



class TicketModel(models.Model):
    
    CITY = {
        ('bosaso to qardho','btq'),
        ( 'bosaso to garowe','btg'),
        ( 'bosaso to galkacyo','btgl'),
        ('bosaso to lascano','btl'),
        ('non', '')
    }
    
   
    
    name = models.CharField(max_length=50, null=True, blank= True)
    to = models.CharField( max_length=255, choices=CITY , default= 'non')
    date = models.DateField(auto_now_add=True)
    go_date = models.DateField(("Date"), default=datetime.date.today)
    total= models.CharField(max_length=50, default='00')
    
    
    
    
    
    
    
    
    
   