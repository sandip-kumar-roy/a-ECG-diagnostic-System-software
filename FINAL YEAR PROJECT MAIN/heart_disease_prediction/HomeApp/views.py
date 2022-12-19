from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from HomeApp.models import register_form
# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=="POST":
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        user_name = request.POST["uname"]
        email_id = request.POST["email"]
        phone_no = request.POST["phone"]
        pwd = request.POST["pwd"]
        c_pwd = request.POST["cpwd"]
        img = request.POST["avatar"]
        gender = request.POST["gender"]
        
        #password matching pwd & cpwd
        if pwd==c_pwd:
            if User.objects.filter(username=user_name).exists():
                print("username already taken")
            elif User.objects.filter(email=email_id).exists():
                print("email alreay taken")
            else:
                usr = User.objects.create_user(username=user_name,password=pwd,email=email_id,first_name=first_name,last_name=last_name)
                usr.save()
                reg = register_form(user=usr,firstname=first_name,lastname=last_name,username=user_name,email=email_id,phone=phone_no,pwd=pwd,cpwd=c_pwd,img=img,gender=gender )
                reg.save()
                return redirect("/")
        else:
            print("pasword not matching")
            return render(request,'register.html')
    else:
        return render(request,'register.html')

def profile(request):
    return render(request,'profile.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')

def predform(request):
    return render(request,'predictionform.html')

def team(request):
    return render(request,'team.html')

def result(request):
    return render(request,'result.html')