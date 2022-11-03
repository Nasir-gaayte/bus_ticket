from re import T
from venv import create
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
    
    

    for tick in tickets:
        print(tick.to)
        costs = tick.to 
        
        y = ''
        if costs == 'bosaso to qardho' :
                y = 10
               
            
        elif costs== 'bosaso to garowe' :
                y= 20
                
        
        elif costs == 'bosaso to galkacyo':
                y = 40
               
            
        elif costs== 'bosaso to lascano':
                y = 30
                
        else: 
            y = 0
                 
    
    tick.cost = y
    tick.save()
    cost= y
   
    return render(request,'core/ticket_details.html',{
        'tickets':tickets,
        'cost':cost,
                })



def get_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details')
    form = TicketForm()
    return render(request,'core/add_ticket.html',{'form':form,
                                                   } )        
    
    
    
    
# class Add_ticket(generic.CreateView):
#     model= TicketModel
#     form_class= TicketForm
#     template_name= 'core/add_ticket.html'
#     success_url= 'detail'            


def costumer_detail(request, id):
    costumer = TicketModel.objects.get(pk = id)
    return render(request,'core/costumer_detail.html',{'costumer':costumer})