from urllib.parse import urlparse
import django


from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
]
