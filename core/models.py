from django.db import models
from django.forms.widgets import NumberInput
import datetime


# Create your models here.


class TicketModel(models.Model):
    CITY = {
        ('bosaso to qardho', 'bosaaso to qardho'),
        ('bosaso to garowe', 'bosaaso to gaowe'),
        ('bosaso to galkacyo', 'bosaso to galkacyo'),
        ('bosaso to lascano', 'bosaso to lascano'),
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
        return self.name + self.cost