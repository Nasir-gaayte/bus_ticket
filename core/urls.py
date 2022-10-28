from django.urls import path 
from . import views
# from core.views import Add_ticket

urlpatterns = [
    path('',views.home,name='home'),
    path('details/',views.tickets_detail,name='details'),
    path('add_ticket/',views.get_ticket,name='add_ticket'),
    # path('add_ticket/',Add_ticket.as_view(),name='add_ticket'),
]
