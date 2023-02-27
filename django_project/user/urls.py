from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', index,name='index'),
    path('patientsignup', patientSignUpView.as_view(), name='patient_signup'),
    path('healthworkersignup', healthworkerSignUpView.as_view(), name='healthworker_signup')
    ,path('patientpage', views.patientpage, name='patientpage'),
    path('loginpatient/',views.Loginpatient,name='loginpatient'),
    path('loginhealthworker/',views.Loginhealthworker,name='loginhealthworker'),
    path('healthworkerpage', views.healthworkerpage, name='healthworkerpage')
]