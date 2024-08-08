from django.shortcuts import render,redirect
from xsolution.models import contact
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm




# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        user=contact(first_name=name,email=email,message=message)
        user.save()
        
        messages.success(request,'Your Message Successfully Updated')
        return render(request,'xsolution/index.html')
    return render(request,'xsolution/index.html')

def services(request):
    return render(request,'xsolution/services.html')

def signup(request):
    return render(request,'xsolution/signup.html')
def blog(request):
    return render(request,'xsolution/blog.html')

def aboutus(request):
    return render(request,'xsolution/about.html')
def contacts(request):
    if request.method=="POST":
        help=request.POST['help']
        industry=request.POST['industry']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        phone=request.POST['phone']
        email=request.POST['email']
        company=request.POST['company']
        message=request.POST['message']
        user=contact(help=help,industry=industry,first_name=first_name,last_name=last_name,phone=phone,email=email,company=company,message=message)
        user.save()
        
        messages.success(request,'Your Message Successfully Updated')
        return render(request,'xsolution/contact.html')
        

    return render(request,'xsolution/contact.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    if request.method=='POST':
        username=request.POST['user_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        user=User.objects.filter(username=username)
        
        if len(username)>10:
            messages.error(request,'Username Lenght not be Greater than 10')
            return render(request,'xsolution/signup.html')
            
        elif not username.isalnum:
            messages.error(request,'Username Character Alpha numeric ')
            return render(request,'xsolution/signup.html')
        elif password1!=password2:
            messages.error(request,'Password does not Match')
            return render(request,'xsolution/signup.html')
        elif user:
            messages.error(request,'user already exists')
            return render(request,'xsolution/signup.html')
        
        
        else:


            newuser=User.objects.create_user(username=username,email=email,password=password1)
            newuser.save()
            messages.success(request,'Account Createted Succesfully')
            return redirect('/login/')
        
    return render(request,'xsolution/signup.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    
    if request.method=='POST':
        uname=request.POST['user_name']
        upass=request.POST['password']
        user=authenticate(username=uname,password=upass,)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully Login')
            return redirect('/dashboard/')
        else:
            messages.error(request,'incorrect username password')
            return redirect('/login/')



    return render(request,'xsolution/login.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'xsolution/dashboard.html')
    else:
        return redirect('/login/')
def user_change(request):
    if request.user.is_authenticated:
        fm=UserChangeForm()
        return render(request,'xsolution/change.html',{'form':fm})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'succesfully logout')
        return redirect('/login/')
    else:
        return redirect('/login/')
        
def change_passwod(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Password change succesfully')
                
                
                update_session_auth_hash(request,fm.user)
                return redirect('/dashboard/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'xsolution/changepass.html',{'form':fm})
    else:
        return redirect('/login/')
    

    
    
    

