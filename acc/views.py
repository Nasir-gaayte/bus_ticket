from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView 
from django.views import generic
# Create your views here.

class Reg(generic.CreateView):
    model= User
    form_class= UserCreationForm
    template_name= 'acc/register.html'
    # success_url= redirect('home')
    
    
    
def log(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    form = AuthenticationForm()
    return render(request,'acc/login.html',{'form':form})




def logout_req(request):
    logout(request)
    return redirect('login')   



       