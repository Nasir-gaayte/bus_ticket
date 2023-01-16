from rest_framework import generics
from core.serializer import Ticketserializer
from core.models import TicketModel



class TicketApiList(generics.ListCreateAPIView):
    queryset = TicketModel.objects.all()
    serializer_class = Ticketserializer
    
    
class TicketApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TicketModel.objects.all()
    serializer_class = Ticketserializer
    lookup_field = 'id'
