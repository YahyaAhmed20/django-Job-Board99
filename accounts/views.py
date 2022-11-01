
from urllib import request
from django.shortcuts import redirect, render
from .forms import Signup,UserForm,ProfileForm
from django.contrib.auth import authenticate,login
from .models import Profile

def signup(request):
    if request.method == 'POST':
        form=Signup(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            login=(request,user)
            return redirect('/accounts/profile')
    else:
        form=Signup()
    
    return render(request,'registration/signup.html',{'form':form})


def profile(request):
    profile=Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})

def profile_edit(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform=UserForm(request.POST,instance=request.user)
        profleform=ProfileForm(request.POST,instance=profile)
        if userform.is_valid() and profleform.is_valid():
            userform.save()
            myprofile=profleform.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            return redirect('accounts:profile')

    else:
        userform=UserForm(instance=request.user)
        profleform=ProfileForm(instance=profile)
    
    return render(request,'accounts/profile_edit.html',{'userform':UserForm,'profleform':ProfileForm})

