from contextlib import nullcontext
from email.policy import default
from logging.config import valid_ident
from multiprocessing.sharedctypes import Value
from optparse import Values
from pickle import GLOBAL
from re import T
from secrets import choice
from tabnanny import verbose
from typing import ValuesView
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
        ('non', 'non')
    }
    
    
    
    
    name = models.CharField(max_length=50, null=True, blank= True)
    to = models.CharField('toto', max_length=255, choices=CITY , default= 'non')
    date = models.DateField(auto_now_add=True)
    go_date = models.DateField(("Date"), default=datetime.date.today)
    cost= models.CharField(max_length=255, default=[])
    
    
   
    
    
            
                        
    
    
    
    
    
    
    
    
    
   