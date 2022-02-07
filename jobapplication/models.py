
from django.db import models
class Carrers(models.Model):
    job_title=models.CharField(max_length=30,editable=True)
    experience_reqiured=models.IntegerField(default='0',editable=True)
    req_skills=models.CharField(max_length=100,default='skills required',null=False,editable=True)
    job_description=models.TextField(max_length=5000,null=True,editable=True)
    contact_no=models.CharField(max_length=10,editable=True,default='0000000')
    updated_time = models.DateTimeField(auto_now_add=False,auto_now=True)
    job_id=models.CharField(max_length=8,default=0)
    job_location=models.CharField(max_length=15,default='location')

class Contact(models.Model):
    firstname=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    message=models.CharField(max_length=1000)
    mobno=models.CharField(max_length=13,default='')
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return self.firstname

