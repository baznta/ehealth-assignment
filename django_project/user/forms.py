from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import patient, healthworker,User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
class patientSignUpForm(UserCreationForm):
    
    phoneno=forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'phoneno', 'password1', 'password2']
    @transaction.atomic
    def save(self):
        user = super().save(commit=True)
        
        user.is_patient = True
        user.save()
        pat = patient.objects.create(user=user)
        
        pat.save()
        return pat
    


class healthworkerSignUpForm(UserCreationForm):
    
    phoneno=forms.CharField(required=True)
    email = forms.EmailField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [ 'email', 'phoneno', 'password1', 'password2']
 
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        
        user.is_healthworker = True
        user.save()
        health = healthworker.objects.create(user=user)
        
        
            
            
        health.save()
 
        return health
    


class LoginForm(AuthenticationForm):
    email = forms.CharField(label='Email')


