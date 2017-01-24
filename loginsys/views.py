# -*-coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf


# Create your views here.
def login(request):
    args={}
    args.update(csrf(request))
    if request.POST:
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/idea')
        else:
            args['login_error']="Пользователь не найдкн"
            return render(request,'login.html',args)
    else:
        return render(request,'login.html',args)

def logout(request):
    back_url = request.META['HTTP_REFERER']
    auth.logout(request)
    return redirect(back_url)

def register(request):
    args = {}
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm()
        args.update(csrf(request))
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = UserCreationForm()
    return render(request,'register.html', args)

