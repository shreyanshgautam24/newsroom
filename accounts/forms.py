from django import forms
from django.contrib.auth import (
    authenticate,get_user_model)

user=get_user_model()
class Userloginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user=auhenticate(username=username,password=password)

            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active():
                raise forms.ValidationError('This user is not active')
        return super(Userloginform,self).clean(*args,**kwargs)

class Userregistrationform(forms.ModelForm):
    email1=forms.EmailField(label='email address')
    email2=forms.EmailField(label='confirm address')
    password=forms.CharField(widget=forms.PasswordInput,label='Password')

    class meta:
        model=user
        fields=[
            'username',
            'email1',
            'email2',
            'password'
        ]
    def clean(self,*args,**kwargs):
        email1=self.changed_data.get('email1')
        email2 = self.changed_data.get('email2')
        password = self.changed_data.get('password')
        if email1!=email2:
            raise forms.ValidationError("Email's must match")
        email_qs=user.objects.filter(email=email)
        if emai_qs.exist():
            raise forms.ValidationError("Email already exist")
        return email