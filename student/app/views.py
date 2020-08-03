from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'index.html')


def handleSignup(request):
    if request.method == 'POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1 != pass2:
            messages.error(request,"Password not matching,Please Try Again!")
            return redirect("/signup")
        try:
            if User.objects.get(username=username):
                messages.warning(request,"UserName Already Taken.")
                return redirect('/signup')
        except Exception as identifier:
             pass    

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.info(request,"SignUp Successfull")
        return redirect("/login")
    return render(request,'signup.html')

def handleLogin(request):

    if request.method == 'POST':
        username=request.POST['username']
        pass1=request.POST['pass1']
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.info(request,"Login Successfull")
            return redirect("/")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("/login")
    return render(request,'login.html')

def handleForgotpassword(request):
    if request.method == 'POST':
        username=request.POST['username']
        pass3=request.POST['pass3']
        pass4=request.POST['pass4']
        if pass3 != pass4:
            messages.error(request,"Please Enter Correct Password!")
            return redirect("/forgotpassword")
        else:
         messages.info(request,"Password Changed Successfully!")
         return redirect("/login")    
    return render(request,'forgotpassword.html')

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Successfull")
    return redirect('/login')