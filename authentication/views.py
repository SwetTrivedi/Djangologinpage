from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
# from django . contrib. auth.forms import UserCreationForm 


# def sign_up(request):
#     if request=='POST':
#          fm=UserCreationForm(request.POST)
#          if fm.is_valid():
#              fm.save()
#     else:
#         fm=UserCreationForm()

#     return render(request,'authentication.html',{'form':fm})


# This is second method

from . forms import signup
# from django.contrib import messages
def sign_up(request):
    if request.method=='POST':
         fm=signup(request.POST)
         if fm.is_valid():
            messages.success(request,'Registraton Sucessfully !!! ')
            fm.save()
            #  messages.add_message(request,messages.SUCCESS,'Registartion Sucessfully !!')
    else:
        fm=signup()
    return render(request,'authentication.html',{'form':fm})

# login page
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
def userlogin(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request," login  sucessfully  ")
                return HttpResponseRedirect("/profile/")
    else:
        fm=AuthenticationForm()
    return render(request,'userlogin.html',{'form':fm})


# profile page
from .forms import Edituser,EditAdmin
def profile(request):
    if request.user.is_authenticated:
        #this code is edit form
        if request.method=='POST':

            if request.user.is_superuser==True:
                fm=EditAdmin(request.POST ,instance=request.user)
            else:
                fm=Edituser(request.POST ,instance=request.user)
            if fm.is_valid():
                messages.success(request,"Updated Sucessfully!!")
                fm.save()

        else:
            if request.user.is_superuser==True:
                fm =EditAdmin(instance=request.user)
            else:
                fm=Edituser(instance=request.user)
        return render(request,'sucess.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')



#logout page

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# password with old password form  change
from django.contrib.auth.forms import PasswordChangeForm

def userpasschange(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.info(request,"  Updated Sucessfully  ")
                return HttpResponseRedirect('/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'change.html',{'form':fm})
    else:
       return HttpResponseRedirect('/login/')

# this is password change without old password form

from django.contrib.auth.forms import SetPasswordForm
def userpasschange1(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.info(request,"  Updated Sucessfully  ")
                return HttpResponseRedirect('/profile/')
        else:
            fm=SetPasswordForm(user=request.user)
        return render(request,'change1.html',{'form':fm})
    else:
       return HttpResponseRedirect('/login/')
    