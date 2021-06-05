from django.shortcuts import render,redirect


from .models import reservation,buffet,items,menu

# Create your views here.
def index(request):
        oitems = items.objects.filter(keep = True)
        omenu = menu.objects.filter(keep = True)
        return render( request,'index.html',{ 'items' : oitems ,'menu':omenu})


def registrationsubmit(request):
        first_name = request.POST['firstname']
        last_name = request.POST['secondname']
        email = request.POST['email']
        phone = request.POST['phone']
        noofguests = request.POST['nofguests']
        rdate = request.POST['rdate']
        rtime = request.POST['rtime']
        reservationtype = request.POST['rtype']
        discription = request.POST['mentions']
        reservationobject = reservation(first_name=first_name, last_name=last_name, email=email, phone=phone , noofguests= noofguests ,rdate=rdate, rtime=rtime, reservationtype=reservationtype, mention=discription)
        reservationobject.save()
        print('user created')
        return redirect('/#reservation')

def buffetsubmit(request):
        bdate = request.POST['date']
        btime = request.POST['time']
        partysize = request.POST['quantity']
        bfirst_name = request.POST['fname']
        blast_name = request.POST['lname']
        bemail = request.POST['email']
        bphone = request.POST['phone']
        blocation = request.POST['location']
        address = request.POST['message']
        buffetobject = buffet(bdate=bdate, btime=btime , partysize=partysize , bfirst_name=bfirst_name , blast_name=blast_name ,bemail=bemail, bphone=bphone , blocation=blocation , address=address)
        buffetobject.save()
        print('user created')
        return redirect('/#booking')