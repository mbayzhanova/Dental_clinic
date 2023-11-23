from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, logout
from account.models import CustomUser
from account import forms


def login(request):
    form = forms.CustomLoginForm()
    if request.method == 'POST':
        form = forms.CustomLoginForm(request = request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print("jnnkjnj")
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                print('form', user)
        else:
            print('form_in_valid', form)
    return render(request, 'account/login.html', { 'form': form})


def my_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    form = forms.CustomUserForm()
    if request.method == 'POST':
        print('ddd', request.POST)
        form = forms.CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.save()
            return redirect('login')
        
    return render(request, "account/register.html", { 'form': form})
