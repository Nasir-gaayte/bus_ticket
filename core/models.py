from contextlib import nullcontext
from email.policy import default
from django.db import models

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
    to = models.CharField('to', max_length=255, choices=CITY , default= 'non')
    date = models.DateField(auto_now_add=True)
    total= models.CharField(max_length=50, default='00')
    
   