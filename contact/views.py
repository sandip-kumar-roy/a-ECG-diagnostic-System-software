from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
from django.contrib.auth.models import User,auth
from HomeApp.models import register_form
from contact.models import contact_form
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def contact_us(request):
    if request.method == 'POST':
        fn=request.POST["fname"]
        ln=request.POST["lname"]
        mail=request.POST["email"]
        ph=request.POST["phone"]
        msg=request.POST["message"]
        

        #updating the user table
        
        #updating the database
        con = contact_form()
        con.firstnm = fn
        con.lastnm = ln
        con.mail = mail
        con.contact = ph
        con.mesg = msg
        con.save()
       
        print(request.POST)
        messages.info(request,' YOUR QUERRY WAS SEND SUCCESSFULLY')
        return render(request,'contact.html')
    else:
        check = register_form.objects.filter(user__id=request.user.id)
        if request.user.is_anonymous:
            return render(request,'contact.html')
        elif len(check)==0:
            messages.info(request,' Admin Cannot View This Page')
            return redirect("msg")
        else:
            return render(request,'contact.html')
        


        
