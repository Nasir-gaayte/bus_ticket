from multiprocessing.spawn import import_main_path
from django.contrib import admin
from .models import TicketModel
# Register your models here.


class TicketAdmin(admin.ModelAdmin):
   
    list_display = ('id', 'name','to', 'date')


admin.site.register(TicketModel, TicketAdmin)