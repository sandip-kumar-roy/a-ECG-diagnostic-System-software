from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect,JsonResponse
from HomeApp.models import register_form
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.mail import send_mail,EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
# Create your views here.



def home(request):
    if "user_id" in request.COOKIES:
        uid = request.COOKIES["user_id"]
        usr = get_object_or_404(User,id=uid)
        login(request,usr)
        return render(request,'home.html')
    return render(request,'home.html')

def register(request):
    if request.method=="POST":
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        user_name = request.POST["uname"]
        email_id = request.POST["email"]
        phone_no = request.POST["phone"]
        pwd = request.POST["pwd"]
        img=request.FILES["avatar"]
        c_pwd = request.POST["cpwd"]
        gender = request.POST["gender"]
        
            
        # check for errorneous input
        """ if len(user_name)<10:
            return render(request,'register.html',{'uname':"Username must be at least 10 characters long"})

        if not user_name.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return render(request,'register.html',{'uname':"Username must contains only alphanumeric characters"}) """
        #password matching pwd & cpwd
        if pwd!=c_pwd:
            return render(request,'register.html',{'pw':"password and confirm password doesn't match"})
        
        try:
            if User.objects.get(username=user_name):
                return render(request,'register.html',{'uname':"username already used,enter different username"})
        except Exception as identifier:
            pass
        try:
            if User.objects.get(email=email_id):
                return render(request,'register.html',{'email':"Email id already used,enter different mail id"})
        except Exception as identifier:
            pass
        
        newuser = User.objects.create_user(username=user_name,email=email_id,password=pwd)
        newuser.first_name=first_name
        newuser.last_name=last_name
        
        newuser.save()
        
        un=newuser.username
        user=User.objects.get(username=un)
        login(request,user)
        data = register_form.objects.all()
        nu = register_form(user=newuser,firstname=first_name,lastname=last_name,username=user_name,email=email_id,phone=phone_no,pwd=pwd,cpwd=c_pwd,img=img,gender=gender)
        nu.save()
        messages.info(request,'Thanks For Joining us,now enjoy our website')
        html_content=render_to_string('register_mail.html',{'title':user.username})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives("REGISTRATION SUCCESS",text_content,settings.EMAIL_HOST_USER,[newuser.email])
        email.attach_alternative(html_content,"text/html")
        email.send()
        return HttpResponseRedirect("/")
    return render(request,'register.html')            

def check_user(request):
    if request.method=="GET":
        un = request.GET["unm"]
        check = User.objects.filter(username=un)
        
        if len(check) == 1:
            return HttpResponse("exists")
        else:
            return HttpResponse("User not exists")

def already_registered(request):
    return redirect('login')

from datetime import datetime
# USER LOGIN PART
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            login_un= request.POST["uname"]
            login_pass=request.POST["password"]
            print(request.POST)
            #checking/validating the user using authenticate
            login_user=authenticate(username=login_un,password=login_pass)
            lu=register_form.objects.filter(username=login_un)
            

            if login_user or User.username == login_user:
                login(request,login_user)
                res=HttpResponseRedirect("/")
                if "rememberme" in request.POST:
                    res.set_cookie("user_id",login_user.id)
                    res.set_cookie("date_login",datetime.now())
                    return res
                else:
                    messages.info(request,'Welcome Back,now enjoy our website')
                    return render(request,'message.html')

            else:
                return render(request,"login.html",{"status":"invalid credentials  !!!"})
        else:
            return render(request,"login.html")
    else:
        messages.info(request,'you are already logged in ')
        return render(request,"message.html")


# CREATING NEW PASSWORD
def newpwd(request):
    context={}
    if request.method=='POST':
        un=request.POST["uname"]
        pwd=request.POST["npass"]
        print("hello")
        user= User.objects.get(username = un)
        print(user,"hello")
        user.set_password(pwd)
        user.save()
        context["status"]="Password changed success"
        return render(request,'login.html',context)


# RESETTING THE PASSWORD OF USER

def reset(request):    
    return render(request,'edit_pwd_mail.html')

import random
def reset_pwd_page(request):
    un=request.GET['username']
    try:
        user=get_object_or_404(User,username=un)
        print(user)
        otp=random.randint(1000,9999)
        msz="Dear {} \n {} is your One Time Password (OTP)  \n\n Do not share it with others \n\n THANKS AND REGARDS \nHeart Disease Prediction Portal".format(user.username,otp)
        try:
            email = EmailMessage("Account Verification",msz,to=[user.email])
            email.send()
            return JsonResponse({"status":"sent","email":user.email,"rotp":otp})
        except:
            return JsonResponse({"status":"error"})    
        
    except:
        return JsonResponse({"status":"failed"})



# USER LOGOUT
def user_logout(request):
    logout(request)
    res=HttpResponseRedirect("msg")
    res.delete_cookie("user_id")
    res.delete_cookie("date_login")
    messages.info(request,' You are successfully logged out !! THANK U')
    return res


# SENDING MESSAGES
def msg(request):
    return render(request,'message.html')
  

# USER PROFILE PART
def profile(request):
    context={}
    if not request.user.is_authenticated:
        return render(request,'register.html',{"status":"Create Your Account In order To View Your Profile!!!"})
    else: 
        check = register_form.objects.filter(user__id=request.user.id)
        if len(check)>0:
            data = register_form.objects.get(user__id=request.user.id)
            context["data"]=data
            return render(request,'profile.html',context)
        else:
            messages.info(request,' Admin Cannot View This Page')
            return HttpResponseRedirect("msg")
    

def about(request):
    return render(request,'about.html')



def service(request):
    return render(request,'service.html')


def team(request):
    return render(request,'team.html')

def result(request):
    return render(request,'result.html')