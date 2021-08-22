from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.

def user_login(requst):
    obj = AuthenticationForm(requst, data=requst.POST or None)
    if obj.is_valid():
        user_ = obj.get_user()
        login(requst, user_)
        return redirect("/")
    context = {
        'form': obj,
        'but_label': "login",
        'title': login
    }
    return render(requst, 'login_template/index.html', context)
def user_logout(requst):
    if requst.method=='POST':
        logout(requst)
        return redirect("/login")
    context = {
        'form': None,
        'but_label': "logot",
        'title': 'logout'
    }
    return render(requst, 'account/auth.html', context)

def user_register(requst):
    obj = UserCreationForm(requst.POST or None)
    if obj.is_valid():

        user=obj.save(commit=True)
        user.set_password(obj.cleaned_data.get('password1'))

        return redirect("/login")
    context = {
        'form': obj,
        'but_label': "user_register",
        'title': login
    }
    return render(requst, 'account/auth.html', context)