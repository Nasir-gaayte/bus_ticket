from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('details/',views.tickets_detail,name='details'),
    path('add_ticket/',views.get_ticket,name='add_ticket'),
]
