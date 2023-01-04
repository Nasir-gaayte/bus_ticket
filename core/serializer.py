from rest_framework import serializers
from core.models import TicketModel




class Ticketserializer(serializers.ModelSerializer):
    class Meta:
        model= TicketModel
        fields = '__all__'





