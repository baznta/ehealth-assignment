from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .decorators import patient_required,healthworker_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect
from .models import patient,healthworker,User
from django.views.generic import CreateView
from .forms import patientSignUpForm,healthworkerSignUpForm,LoginForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def patientpage(request):
    return render(request,'patientpage.html')
def healthworkerpage(request):
    return render(request,'healthworkerpage.html')
def loginindex(request):
    return render(request,'loginindex.html')




@method_decorator([login_required, patient_required], name='dispatch')
class patientSignUpView(CreateView):
    model = User
    form_class = patientSignUpForm
    template_name = 'signup.html'
    def registerpatient(self,request):
        if request.method == 'POST':
            form = patientSignUpForm(request.POST)
            if form.is_valid():
                form.save()
                
                email = form.cleaned_data.get('email')
                phone = form.cleaned_data.get('phoneno')
            return redirect('patientpage.html')
        else:
            form = patientSignUpForm()
        return render(request, {'form': form})
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)
@method_decorator([login_required, healthworker_required], name='dispatch')
class healthworkerSignUpView(CreateView):
    model = User
    form_class = healthworkerSignUpForm
    template_name = 'signup.html'
    def registerhealthworker(self,request):
        if request.method == 'POST':
            form = healthworkerSignUpForm(request.POST)
            if form.is_valid():
                form.save()
                
                email = form.cleaned_data.get('email')
                phone = form.cleaned_data.get('phoneno')
                return redirect('healthworkerpage')
        else:
            form = healthworkerSignUpForm()
        return render(request, {'form': form})
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'healthworker'
        return super().get_context_data(**kwargs)



def Loginpatient(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            
            return redirect('patientpage')
        else:
            return redirect('login')
    form = LoginForm()
    return render(request, 'login.html', {'form':form, 'title':'log in'})

def Loginhealthworker(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
        form=LoginForm(request.POST)
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            
            return redirect('healthworkerpage')
        else:
            return redirect('login')
    form = LoginForm()
    return render(request, 'login.html', {'form':form, 'title':'log in'})
