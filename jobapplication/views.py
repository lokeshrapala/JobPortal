# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests

from django.conf import settings
from django.utils import timezone
#import mammoth
from django.shortcuts import render
from django.core.mail import send_mail
import random
from .forms import ContactForm
from .models import Contact, Carrers



from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method=="POST":
     form = ContactForm(request.POST)
     if form.is_valid():
        firstname = form.cleaned_data['firstname']
        email = form.cleaned_data['email']
        mobn=form.cleaned_data['mobno']
        message = form.cleaned_data['message']
        Contact.objects.get_or_create(firstname=firstname, email=email, message=message,mobno=mobn)
        subject='Thankyou for contacting us'
        email_message='we get in few moments'
        From_mail=settings.EMAIL_HOST_USER
        to_list=[email]
        send_mail(subject,email_message,From_mail,to_list,fail_silently=False)
        res=requests.post('https://textbelt.com/text', {
            'phone': mobn,
            'message': 'we get in few moments',
            'key': 'textbelt',
        })
        print(res.json())
        return render(request, 'index.html')
    else:
         return render(request,'index.html')
def ourprojects(request):
    return render(request,'ourprojects.html')
def  careers(request):
    jobs = Carrers.objects.order_by('-id')
    return render(request,"careers.html",{'order': jobs})




