from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.log,name='login'),
    path('register/',views.Reg.as_view(),name='register'),
]
