from django import forms
from .models import Contact,Carrers
class ContactForm(forms.Form):
    firstname=forms.CharField(max_length=20)
    email=forms.EmailField(max_length=50)
    mobno=forms.CharField(max_length=15)
    message=forms.CharField(max_length=1000)
