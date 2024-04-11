from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from user_app.form import RegisterForm, SignupForm, UserImageForm


# Create your views here.


def User_Registration(request):

    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'register.html',{'form':form})


def user_signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'signup.html',{'form':form})


def user_login(request):

    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pswd']

        data = authenticate(username=username,password=password)
        if data is not None:
            return redirect(User_Registration)

    return render(request,'login.html')

def user_logout(request):

    logout(request)
    return redirect(user_login)


def Upload_Images(request):

    if request.method == 'POST':
        form = UserImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = UserImageForm()

    return render(request, 'uploaddata.html', {'form': form})

