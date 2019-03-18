from django.shortcuts import render
from . import forms
from newsroom.models import newsdata

# Create your views here.
def signup(request):
    form=forms.userid()
    if request.method == 'POST':
        form = forms.userid(request.POST)
        if form.is_valid():
            print('Form validation success and printing data')
            print('Email', form.cleaned_data['email'])
            print('Password', form.cleaned_data['password'])
    return render(request,'newsroom/signup.html',{'form':form})
def newsroom(request):
    news=newsdata.objects.all()
    my_dict={'news':news}
    return render(request,'newsroom/newsroom.html',context=my_dict)
def userid(request):
    form=forms.userid()
    if request.method == 'POST':
        form = forms.userid(request.POST)
        if form.is_valid():
            print('Form validation success and printing data')
            print('Email', form.cleaned_data['email'])
            print('Password', form.cleaned_data['password'])
    return render(request,'newsroom/input.html',{'form':form})
