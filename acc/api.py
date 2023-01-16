from rest_framework import generics
from acc.serializer import Userserializer
from django.contrib.auth.models import User


class UserApiList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    
    
class UserApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class= Userserializer
    lookup_field = 'id'    
    
    
    