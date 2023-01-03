from django.views import View
from django.shortcuts import render,redirect
from .models import TicketModel
from .forms import TicketForm
from django.core.mail import send_mail, send_mass_mail





# the templates

def home(request):
    detail= TicketModel.objects.all()
    
    return render(request,'core/home.html', {
        'detail':detail,
        })



def tickets_detail(request):
    tickets = TicketModel.objects.all()
    
   
    

    for tick in tickets:
        print(tick.to)
        costs = tick.to 
        global y
        y = ''
        if costs == 'bosaso to qardho' :
                y =10
               
            
        elif costs== 'bosaso to garowe' :
                y =20
                
        
        elif costs == 'bosaso to galkacyo':
                 y =30
               
            
        elif costs== 'bosaso to lascano':
                 y =40
                
        else: 
            y = 0
        tick.cost = y
        tick.save()
   
    return render(request,'core/ticket_details.html',{
        'tickets':tickets,
        
                })



def get_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            
            send_mail(
                f'mudane/murow {username}',
                f"Fdlan kidir A/C 50000 qimaha ticket ka oo dhan {form.cleaned_data.get('cost')}$" ,
                'doon1wac101@gmail.com',
                [email],
            )
            send_mail(
                f"name  {username} want ticket form  {form.cleaned_data.get('to')}",
                f"pay {form.cleaned_data.get('cost')} $ on {form.cleaned_data.get('date')}",
                email,
                ['doon1wac101@gmail.com'],
            )
            
            

            return redirect('details')
    form = TicketForm()
    return render(request,'core/add_ticket.html',{'form':form,
                                                   } )        
    
# class Add_ticket(generic.CreateView):
#     model= TicketModel
#     form_class= TicketForm
#     template_name= 'core/add_ticket.html'
#     success_url= 'detail'            


def update_ticket(request, id):
    toUp = TicketModel.objects.get(pk=id)
    if request.method == "POST":
        form = TicketForm(request.POST or None, instance=toUp)
        if form.is_valid():
            
            form.save()
            return redirect('details')
    form = TicketForm(instance=toUp)        
    return render(request,'core/update.html',{'form':form,
                                              'toUp':toUp})
    
    
def deleteticket(request, id):
    toDe=TicketModel.objects.get(pk=id)
    toDe.delete()
    return redirect('details')


def costumer_detail(request, id):
    costumer = TicketModel.objects.get(pk = id)
    return render(request,'core/costumer_detail.html',{'costumer':costumer})


