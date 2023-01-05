from django.shortcuts import render,reverse
from django.db.models import Q
from search.models import locate_city
from appointment.models import create_appointment
from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404, get_object_or_404
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
# Create your views here.
def search(request):
    context={}
    all_doctors=locate_city.objects.all()
    if "qry" in request.GET:
        q=request.GET["qry"]
        doctors=locate_city.objects.filter(Q(state__icontains=q) | Q(city__icontains=q))
        context['doctors']=doctors
        context['abcd']='search'
        
    return render(request,'searchresults.html',context)

import random
def book(request,id):
    member = locate_city.objects.get(id=id)
    invoice_id=random.randint(10000,99999)
    amount=float((member.cost)*0.012)
    paypal_dict = {
        'business': settings.PAYPAL_RECIEVER_EMAIL,
        'amount': str(amount),
        'item_name': 'Order {}'.format(member.name),
        'invoice': "INVOICE-NO -"+str(invoice_id),
        
        'notify_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format("127.0.0.1:8000",
                                              reverse('payment_cancelled')),
    }
    # form=PayPalPaymentsForm(initial=paypal_dict)
    
    # saving the payment and booking details
    usr=User.objects.get(username=request.user.username)
    payment=create_appointment(usr_id=usr,doctor_id=id,doctor_name=member.name,invoice_id=invoice_id)
    payment.save()
    request.session["payment_id"]=payment.id
    context={
        'doc':member,
        'form':paypal_dict
        
    }
    return render(request,'appointment.html',context)


def payment_done(request):
    if "payment_id" in request.session:
        pay_id=request.session["payment_id"]
        pay_obj=get_object_or_404(create_appointment,id=pay_id)
        pay_obj.status=True
        pay_obj.save

    return render(request,'payment_success.html')

def payment_cancelled(request):
    return render(request,'payment_failed.html')