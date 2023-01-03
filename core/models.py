from django.db import models
from django.forms.widgets import NumberInput
import datetime


# Create your models here.


class TicketModel(models.Model):
    CITY = {
        ('bosaso to qardho', 'btq'),
        ('bosaso to garowe', 'btg'),
        ('bosaso to galkacyo', 'btgl'),
        ('bosaso to lascano', 'btl'),
        ('non', 'non')
    }

    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    phone = models.IntegerField()
    to = models.CharField('toto', max_length=255, choices=CITY, default='non')
    date = models.DateField(auto_now_add=True)
    go_date = models.DateField()
    cost = models.CharField(max_length=255)

    def __str__(self) :
        return self.name