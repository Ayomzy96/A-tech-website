from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
   
    context = {'signupform':form}

    return render(request, 'signup.html', context=context)



def loginauth(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
            name=user.username
    context={'loginform':form}

    return render(request, 'login.html', context=context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def dashboard(request):
    return render(request, 'dashboard.html')
