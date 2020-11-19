from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

# Create your views here.
#def index(request):
    #return render(request,'blog/index.html')

def info(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('blog:index')
           
            
    else:
        form = UserCreationForm()   
        '''
        fullname = request.POST.get('fname')
        emailads = request.POST.get('ename')
        message  = request.POST.get('mname')
        

        contactmail = Contact(name=fullname, email=emailads, sms=message)
        contactmail.save()
        '''
    return render(request, 'blog/contact.html',{'form':form})

def login_views(request):
    if request.method == 'POST': 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('blog:home')
         
    else:
        form = AuthenticationForm()
    return render(request,'blog/login.html',{'form':form})

def logout_views(request):
    if request.method == 'POST':
        logout(request)
        return redirect('blog:contact')
    
def catagory(request):
    return render(request, 'blog/catagory.html')
