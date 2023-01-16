from django.views import View
from django.shortcuts import render,redirect
from .models import TicketModel
from .forms import TicketForm
from django.core.mail import send_mail


from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from docx import Document
from docx.shared import Inches

# text file 


def text(request, id):
    doc = HttpResponse(content_type='docx/plain')
    doc['Content-Disposition'] = 'attachment; filename=yourticket.docx'
  
    doc.writelines('Ticket Online')
    doc.writelines('welcome to our online serves\n \n')
    doc.writelines('this is your ticket \n \n \n \n ')
    
    lines = []
    tickests = TicketModel.objects.get(id = id)
    lines.append(f"mr/mis {tickests.name} \n your ticket from {tickests.to}\n mack showr you pay {tickests.cost}$  ")
    
    doc.writelines(lines)
    
    
    
    
    return doc
    
    
    



# the templates

def home(request):
    detail= TicketModel.objects.all()
    
    return render(request,'core/home.html', {
        'detail':detail,
        })


@login_required
def tickets_detail(request):
    tickets = TicketModel.objects.all().order_by('-id')
    
   
    

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
            name=form.cleaned_data.get('name')
            print (name)
            email = form.cleaned_data.get('email')
            co = TicketModel.objects.all().filter(cost=cost)
            print(co)
            cost = co
            send_mail(
                f'mudane/murow {name}',
                f"Fdlan kidir A/C 50000 qimaha ticket ka oo dhan {cost}$" ,
                'doon1wac101@gmail.com',
                [email],
            )
            send_mail(
                f"name  {name} want ticket form  {form.cleaned_data.get('to')}",
                f"pay {cost} $ on {form.cleaned_data.get('date')}",
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

@login_required
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
    
@login_required    
def deleteticket(request, id):
    toDe=TicketModel.objects.get(pk=id)
    toDe.delete()
    return redirect('details')

@login_required
def costumer_detail(request, id):
    costumer = TicketModel.objects.get(pk = id)
    return render(request,'core/costumer_detail.html',{'costumer':costumer})


