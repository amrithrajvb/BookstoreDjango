from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from owner.models import Book
# Create your views here.

def signup_view(request):
    form=forms.UserRegistrationForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration successful")
            return redirect('signin')
        else:
            return render(request,"customer/signup.html",{"form":form})
    return render(request,"customer/signup.html",context)


def signin_view(request):
    form=forms.LoginForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('userhome')
            else:
                messages.error(request,"please enter correct username/password")
                return redirect('signin')
        else:
            return render(request,"customer/login.html",{"form":form})

    return render(request,"customer/login.html",context)

def signout(request):
    logout(request)
    return redirect('signin')

def user_home(request):
    book=Book.objects.all()
    context={"books":book}
    return render(request,"customer/userhome.html",context)

