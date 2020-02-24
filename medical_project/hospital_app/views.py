from django.shortcuts import render, redirect
from django.http import HttpResponse
from hospital_app.models import Topic, Webpage,Patient_information, AccessRecord, User_profile,Hospital_list,Appointment_date
from . import forms
from hospital_app.forms import NewUserForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
     
   return render(request, 'temp/index.html')#, context=date_dict)
    
def users(request):
       form = NewUserForm()
       
       if request.method == "POST":
              form = NewUserForm(request.POST)
              
              if form.is_valid():
                     form.save(commit=True)
                     return index(request)
              else:
                     print('ERROR FORM INVALID')
                     
       return render(request, 'temp/users.html', {'form': form})

def login_page(request):
       form = NewUserForm()
       
       if request.method == "POST":
              form = NewUserForm(request.POST)
              
              if form.is_valid():
                     form.save(commit=True)
                     return index(request)
              else:
                     print('ERROR FORM INVALID')
                     
       return render(request, 'temp/login_page.html' , {'form': form})
def homeandh(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    return render(request,'temp/homeandh.html',{ 'title':'Home Page',})
def patient_profile(request):
       return render(request,'temp/patient_profile.html' )
def register(request):
       if request.method == 'POST':
              form = UserCreationForm(request.POST)
              if form.is_valid():
                     full_name = form.cleaned_data.get('first_name')
                     return redirect('blog-home')
       else:
              form = UserCreationForm()
       return render(request, 'temp/sign_up_page.html', {'form': form})
def sign(request):
       return render(request,'temp/sign_up_page.html')
def sign_up_page(request):
       if request.method == 'POST':
       
              full_name = request.POST['first_name']
              email =  request.POST['email']
              create_password =  request.POST['create_password']
              confirm_password = request.POST['confirm_password']
              if create_password==confirm_password:
                     if User.objects.filter(username=username).exists():
                            print("user name taken")
                     elif User.objects.filter(email=email).exists():
                            print("email is taken")
                     else:
                            user = User.objects.create_user(username=username, password = create_password, email=email, full_name = first_name)
                            user.save();
                            print('user created')
                     
              else:
                     print("pattern not matching")
              return redirect('/ ' )
       else:
              return(request, 'temp/sign_up_page.html')
       
def form_name_view(request):
   form = forms.FormName()         
   
   if request.method == 'POST':
          form = forms.FormName(request.POST)
          
          if form.is_valid():
                 #Do something code
                 print("VALIDATION SUCCESS")
                 print("NAME: "+form.cleaned_data['name'])
                 print("EMAIL: "+form.cleaned_data['email'])
                 print("TEXT: "+form.cleaned_data['text'])
   return render(request, 'temp/form_page.html', {'form':form})


def register(request):
       registered = False
       
       if request.method == "POST":
              user_form = UserForm(data=request.POST)
              profile_form = UserProfileInfoForm(data=request.POST)
              
              if user_form.is_valid() and profile_form.is_valid():
                     user = user_form.save()
                     user.set_password(user.password)
                     user.save()
                     
                     profile = profile_form.save(commit=False)
                     profile.user = user
                     
                     if 'profile_pic' in  request.FILES:
                            profile.profile_pic = request.FILES['profile_pic']
                     profile.save()
                     
                     registered = True
              else:
                     print(user_form.errors, profile_form.errors)
       else:
           user_form = UserForm()
           profile_form = UserProfileInfoForm()
           
       return render(request, 'temp/sign_up_page.html', {'user_form':user_form, 
                                                         'profile_form':profile_form,
                                                         'registered':registered})