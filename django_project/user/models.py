from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    is_patient=models.BooleanField(default=False)
    is_healthworker=models.BooleanField(default=False)
    email = models.EmailField(('email address'), unique=True)
class healthworker(models.Model):
    #default=''
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    Phonenumber = models.CharField(max_length =11,name="phone number",unique=True,null=True)
    email = models.EmailField(('email address'),null=True, unique=True)
    def get_absolute_url(self): # new
        return reverse('healthworkerpage')
    

    
class patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    pnonenumber= models.CharField(max_length =11,name="phone number",unique=True,null=True)
    email = models.EmailField(('email address'), unique=True,null=True)
    def get_absolute_url(self): # new
        return reverse('patientpage')
    

   