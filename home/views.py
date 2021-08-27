from users.models import Profile
from home.models import Lecture
from django.shortcuts import render, redirect
# from .models import Train, Ticket
from django.template.loader import render_to_string
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .forms import ticket
from django.conf import settings # new
from django.views.generic.base import TemplateView
from datetime import date
import json
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def starting(request):
    user=request.user
    
    if user:
        profile = Profile.objects.get(user=user)
        result = Lecture.objects.filter(batch=profile.batch).order_by('start_time') 
        print(result)
    return render(request,'home/starting.html',{'user':user,'result':result})

# def search(request,source,destination,date):
#     # date = date.now()
#     print(date)
#     trains=[]
#     trains_with_extra_nodes = []
#     sources = []
#     ptrains = (Train.objects.filter(source__iexact=source))
#     for i in ptrains:
#         basic=[]
#         print(i.destination.upper())
#         if(i.destination.upper() == destination.upper()):
#             basic.append(i)
#             ticketcheck = Ticket.objects.filter(date=date)
#             countticket =0
#             for j in ticketcheck:
#                     if(j.train == i):
#                             countticket=countticket+1
#             basic.append(countticket)
#             i.count=3-countticket
#             if i.count<=0:
#                     z="WL "
#                     i.count=str((-i.count)+1)
#                     i.count =z+i.count
#             i.date = date
#             print(i)
#             trains.append(i)
#         else :
#             basic.append(i)
#             ticketcheck = Ticket.objects.filter(date=date)
#             countticket =0
#             for j in ticketcheck:
#                     if(j.train == i):
#                             countticket=countticket+1
#             basic.append(countticket)
#             i.count=3-countticket
#             if i.count<=0:
#                     z="WL "
#                     i.count=str((-i.count)+1)
#                     i.count =z+i.count
#             i.date = date
#             sources.append(i)


#     for sou in sources:
#         ptrains = (Train.objects.filter(source__iexact=sou.destination))
#         for i in ptrains:
#             basic=[]
#             print(i.destination.upper())
#             if(i.destination.upper() == destination.upper() and i.departure_time>sou.arrival_time):
#                 basic.append(i)
#                 ticketcheck = Ticket.objects.filter(date=date)
#                 countticket =0
#                 for j in ticketcheck:
#                         if(j.train == i):
#                                 countticket=countticket+1
#                 basic.append(countticket)
#                 i.count=3-countticket
#                 if i.count<=0:
#                         z="WL "
#                         i.count=str((-i.count)+1)
#                         i.count =z+i.count
#                 i.date = date
#                 train_with_one_node = {
#                     'first_train' : sou,
#                     'second_train' : i
#                 }
#                 trains_with_extra_nodes.append(train_with_one_node)
#                 break

#     print(trains_with_extra_nodes)
#     print("jbfjbjhfbdubcd")
#     context={'trains':trains, 'trains_with_extra_nodes': trains_with_extra_nodes}
#     return render(request,'home/search.html',context)

# def ticketbook(request,id,date):
#     train = Train.objects.filter(id=id).first()
#     train.date=date
#     print("ticketbokk")
#     print(date)
#     return render(request,'home/book.html',{'train':train})

# def ticketbk(request,id,date):
#     print("aayay habhah")    
#     form = ticket()
#     key = settings.STRIPE_PUBLISHABLE_KEY
#     train = Train.objects.filter(id=id).first()
#     train.date=date
#     amount = train.amount
#     return render(request,'home/tick.html',{'form':form, 'key':key, 'amount':amount})

# def realbook(request,id,date):
#     if request.method == 'POST':
#         form = ticket(request.POST)
#         if form.is_valid():
#             passenger_name = form.cleaned_data.get('passenger_name')
#             age = form.cleaned_data.get('age')
#             print(passenger_name)
#         user=request.user
#         train = Train.objects.filter(id=id).first()
#         tcount = Ticket.objects.filter(date=date)
#         g=0
#         seatnos=[]
#         for i in range(1,20):
#             seatnos.append(0)
#         for i in tcount:
#                 if i.train == train:
#                         seatnos[i.seatno]=1;
#                         g=g+1
#         if g>=3:
#                 status = "Waiting List"
#                 seatno = 15
#         # return render(request,'home/starting.html')
#         else:
#             for i in range(1,4):
#                 if seatnos[i]==0:
#                     seatno=i
#                     break
#             status = "Confirm"
#         o = str(date)
#         p = o[0:4]
#         p = p + o[5:7]
#         p = p + o[8:11]
#         z = Ticket.objects.all()
#         po = z.count()
#         po = str(po)
#         print(po)
#         pnr = str(train.id)+p+str(user.id)+po
#         # passenger_name = request.POST.get('name',None)
#         # age = request.POST.get('age',None)
#         ticke = Ticket(user=user,
#         pnr=pnr,status=status,date=date,train=train,passenger_name=passenger_name,
#         age=age,seatno=seatno
#         )
#         ticke.save()
#         print(ticke)
#         messages.success(request, f'You Ticket has been Booked Successfully')
#         return redirect('tickt', pnr=pnr)

# def ticketbook2(request,id1,id2,date):
#     train1 = Train.objects.filter(id=id1).first()
#     train2 = Train.objects.filter(id=id2).first()
#     train1.date=date
#     print("ticketbokk")
#     print(date)
#     return render(request,'home/book2.html',{'train1':train1,'train2':train2})

# def ticketbk2(request,id1,id2,date):
#     print("aayay habhah")    
#     form = ticket()
#     key = settings.STRIPE_PUBLISHABLE_KEY
#     train1 = Train.objects.filter(id=id1).first()
#     train2 = Train.objects.filter(id=id2).first()
#     train1.date=date
#     amount = train1.amount + train2.amount
#     return render(request,'home/tick2.html',{'form':form, 'key':key, 'amount':amount})

# def realbook2(request,id1,id2,date):
#     if request.method == 'POST':
#         form = ticket(request.POST)
#         if form.is_valid():
#             passenger_name = form.cleaned_data.get('passenger_name')
#             age = form.cleaned_data.get('age')
#             print(passenger_name)
#         user=request.user
#         train1 = Train.objects.filter(id=id1).first()
#         tcount = Ticket.objects.filter(date=date)
#         g=0
#         seatnos=[]
#         for i in range(1,20):
#             seatnos.append(0)
#         for i in tcount:
#                 if i.train == train1:
#                         seatnos[i.seatno]=1;
#                         g=g+1
#         if g>=3:
#                 status = "Waiting List"
#                 seatno = 15
#         # return render(request,'home/starting.html')
#         else:
#             for i in range(1,4):
#                 if seatnos[i]==0:
#                     seatno=i
#                     break
#             status = "Confirm"
#         o = str(date)
#         p = o[0:4]
#         p = p + o[5:7]
#         p = p + o[8:11]
#         z = Ticket.objects.all()
#         po = z.count()
#         po = str(po)
#         print(po)
#         pnr = str(train1.id)+p+str(user.id)+po
#         # passenger_name = request.POST.get('name',None)
#         # age = request.POST.get('age',None)
#         ticke = Ticket(user=user,
#         pnr=pnr,status=status,date=date,train=train1,passenger_name=passenger_name,
#         age=age,seatno=seatno
#         )
#         ticke.save()
#         print(ticke)

#         train2 = Train.objects.filter(id=id2).first()
#         tcount = Ticket.objects.filter(date=date)
#         g=0
#         seatnos=[]
#         for i in range(1,20):
#             seatnos.append(0)
#         for i in tcount:
#                 if i.train == train2:
#                         seatnos[i.seatno]=1;
#                         g=g+1
#         if g>=3:
#                 status = "Waiting List"
#                 seatno = 15
#         # return render(request,'home/starting.html')
#         else:
#             for i in range(1,4):
#                 if seatnos[i]==0:
#                     seatno=i
#                     break
#             status = "Confirm"
#         o = str(date)
#         p = o[0:4]
#         p = p + o[5:7]
#         p = p + o[8:11]
#         z = Ticket.objects.all()
#         po = z.count()
#         po = str(po)
#         print(po)
#         pnr = str(train2.id)+p+str(user.id)+po
#         # passenger_name = request.POST.get('name',None)
#         # age = request.POST.get('age',None)
#         ticke = Ticket(user=user,
#         pnr=pnr,status=status,date=date,train=train2,passenger_name=passenger_name,
#         age=age,seatno=seatno
#         )
#         ticke.save()
#         print(ticke)
#         messages.success(request, f'You Ticket has been Booked Successfully')
#         return redirect('booking')


# def tickt(request,pnr):    
#     tic = Ticket.objects.filter(pnr=pnr).first()
#     print(tic)
#     if tic == None:
#         return render(request,'home/notick.html')
#     return render(request,'home/ticke.html',{'tic':tic})

# def canceltic(request,pnr):
#     tic = Ticket.objects.filter(pnr=pnr).first()
#     if(tic.user == request.user):
#         if tic.status == "Confirm":
#             print("oihv")
#             t = tic.seatno
#             seatnos=[]
#             tics = Ticket.objects.filter(date=tic.date)
#             for ti in tics:
#                 print(ti.status)
#                 if ti.status == "Waiting List":
#                     ti.seatno=t
#                     ti.status="Confirm"
#                     ticket = Ticket(user=ti.user,
#                     pnr=ti.pnr,status="Confirm",date=ti.date,train=ti.train,passenger_name=ti.passenger_name,
#                     age=ti.age,seatno=t
#                     )
#                     ticket.save()
#                     ti.delete()
#                     break
#         tic.delete()
#     messages.success(request, f'You Ticket has been Cancelled Successfully')
#     return redirect('home-home')

# def pnrstatus(request):
#     if request.method == 'POST':
#         pnr = request.POST.get('pnr',None)
#         print(pnr)
#         return redirect('tickt', pnr=pnr)
#     else :
#         return render(request,'home/pnrstatus.html')


# def about(request):
#     return render(request,'home/about.html')


# def payment(request):
#     key = settings.STRIPE_PUBLISHABLE_KEY
#     return render(request,'home/payment.html',{'key':key})

# def booking(request):    
#     tic = Ticket.objects.filter(user=request.user)
#     return render(request,'home/booking.html',{'tic':tic})