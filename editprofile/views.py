from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect
from HomeApp.models import register_form
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def edit_profile(request):
    context = {}
    data = register_form.objects.get(user__id=request.user.id)
    context["data"]=data
    if request.method=="POST":
        fn=request.POST["fname"]
        ln=request.POST["lname"]
        un=request.POST["uname"]
        mail=request.POST["email"]
        ph=request.POST["phone"]
        age=request.POST["age"]
        ct=request.POST["city"]
        gen=request.POST["gender"]
        occ=request.POST["occupation"]

        usr = User.objects.get(id = request.user.id)

        #updating the user table
        usr.first_name=fn
        usr.last_name=ln
        usr.user_name=un
        usr.email = mail
        usr.save()

        #updating the register table
        data.phone = ph
        data.gender = gen
        data.username=un
        data.age=age
        data.city=ct
        data.occupation=occ
        if "image" in request.FILES:
            img=request.FILES["image"]
            data.img=img
        data.save()
        
        #updating the profile pic
        
        print(request.FILES)
        context["status"]="Your Profile Updated Successfully. Thankyou!!"
    return render(request,'editprofile.html',context)

def profile_base(request):
    context = {}
    check = register_form.objects.filter(user__id=request.user.id)
    if len(check)>0:
        data = register_form.objects.get(user__id=request.user.id)
        context["data"]=data
        return render(request,'profilebase.html',context)
    else:
        messages.info(request,' Admin Cannot View This Page')
        return HttpResponseRedirect("msg")

def edit_profile_password(request):
    context = {}
    if request.method=="POST":
        mail=request.POST["email"]
        new_pass=request.POST["npwd"]
        cnew_pass=request.POST["ncpwd"]

        user = User.objects.get(id=request.user.id)
        un=user.username
        p=new_pass
        user.set_password(new_pass)
        context["msg"]="PASSWORD CHANGED SUCCESSFULLY"
        user.save()
        user=User.objects.get(username=un)
        login(request,user)
    data = register_form.objects.get(user__id=request.user.id)
    context["data"]=data
    return render(request,'changepassword.html',context)
