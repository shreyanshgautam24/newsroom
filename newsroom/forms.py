from django import forms
class userid(forms.Form):
     email=forms.CharField(max_length=100)
     password=forms.CharField(min_length=8)


class FeedBackForm(forms.Form):
     name=forms.CharField()
     rollno=forms.IntegerField()
     email=forms.EmailField()
     feedback=forms.CharField(widget=forms.Textarea)
