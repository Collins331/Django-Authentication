from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm

####### Django Authentication ######
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(requests):
    return render(requests, 'people/index.html')


def register(requests):
    
    form = CreateUserForm()
    if requests.method == "POST":
        form = CreateUserForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'registerform': form}
    return render(requests, 'people/register.html', context=context)


def login(requests):
    form = LoginForm()
    
    if requests.method == 'POST':
        form = LoginForm(requests, data=requests.POST)
        
        if form.is_valid():
            username = requests.POST.get('username')
            password = requests.POST.get('password')
            
            user = authenticate(requests, username=username, password=password)
            
            if user is not None:
                auth.login(requests, user)
                return redirect('dashboard')
            
    context= {'loginform': form}
    return render(requests, 'people/login.html', context=context)
@login_required(login_url='login')
def dashboard(requests):
    return render(requests, 'people/dashboard.html')


def user_logout(requests):
    auth.logout(requests)
    return redirect('/')
