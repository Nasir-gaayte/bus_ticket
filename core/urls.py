from django.urls import path 
from . import views
from core import api
# from core.views import Add_ticket

urlpatterns = [
    path('',views.home,name='home'),
    path('details/',views.tickets_detail,name='details'),
    path('add_ticket/',views.get_ticket,name='add_ticket'),
    path('costumer_detail/<int:id>/',views.costumer_detail,name='costumer_detail'),
    path('update/<id>/',views.update_ticket,name='update'),
    path('delete/<id>/',views.deleteticket,name='delete'),
    path('doc/<int:id>/',views.text,name='doc'),
    path('ApiList/',api.TicketApiList.as_view(),name='ApiList'),
    path('ApiDetail/<int:id>/',api.TicketApiDetail.as_view(),name='ApiDetail'),
]
