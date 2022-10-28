from re import T
from django.shortcuts import render,redirect
from .models import TicketModel
from .forms import TicketForm
from django.views import generic 
from django.views.generic import CreateView

# Create your views here.


def home(request):
   
    
    return render(request,'core/home.html')



def tickets_detail(request):
    tickets = TicketModel.objects.all()
    wear = TicketModel.objects.filter()
    print(wear)
    return render(request,'core/ticket_details.html',{'tickets':tickets})



def get_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details')
    form = TicketForm()
    return render(request,'core/add_ticket.html',{'form':form})        
    
    
    
    
# class Add_ticket(generic.CreateView):
#     model= TicketModel
#     form_class= TicketForm
#     template_name= 'core/add_ticket.html'
#     success_url= 'detail'            