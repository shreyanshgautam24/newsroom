from django.shortcuts import render, redirect
from .forms import Userloginform,Userregistrationform
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import (
get_user_model,authenticate,login,logout)
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})



def login_view(request):
    action=request.GET.get('action')
    form=Userloginform(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password= form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        if action:
            return redirect(action)
        return redirect('/')
    return render(request ,'accounts/login.html',{'form':form})
