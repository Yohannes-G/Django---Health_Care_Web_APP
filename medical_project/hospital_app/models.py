from django.db import models
from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class  Topic(models.Model):
    top_name = models.CharField(max_length=254,  unique = True)
    
    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.DO_NOTHING)
    name = models.CharField( max_length=254, unique = True)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name
     
class AccessRecord(models.Model):
    name = models.ForeignKey(  'Webpage', on_delete=models.DO_NOTHING)
    date = models.DateField()
    
    def __str__(self):
        return str(self.date)

class User_profile(models.Model):
    first_name =  models.CharField(max_length=128) 
    last_name = models.CharField(max_length= 128 )
    email = models.EmailField(max_length=254, unique = True)
    
    def __str__(self):
        return str(self.first_name)
class sign_up_page(models.Model):
    full_name =  models.CharField(max_length=128) 
    email = models.EmailField(max_length=254, unique = True)
  #  phone_number = PhoneNumberField( )
    job = models.CharField(max_length=128)
    #create_password =  
class Hospital_list(models.Model):
    hospital_id = models.CharField(max_length=128)
    hospital_name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, unique = True)
    
    def __str__(self):
        return str(self.hospital_name)
class Appointment_date(models.Model):
    hospital_list = models.ForeignKey(  'Hospital_list', on_delete=models.DO_NOTHING)
    patient_id = models.CharField(max_length=128)
    patient_name = models.CharField(max_length=128)
    email =models.EmailField(max_length=254, unique = True)
    date = models.DateField()
    
    def __str__(self):
        return str(self.date)
class Patient_information(models.Model):
    #patient_hospital = models.ForeignKey(  'Hospital_list', on_delete=models.DO_NOTHING)
    #patients_appoint = models.ForeignKey(  'Appointment_date', on_delete=models.DO_NOTHING)
    first_name =  models.CharField(max_length=128) 
    last_name = models.CharField(max_length= 128 )
    age = models.IntegerField( )
    sex = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    phone = models.IntegerField( )
    street_address = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, unique = True)
    
    
    def __str__(self):
        return str(self.first_name)
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    
    #additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(  upload_to='profile_pics',  blank=True)
    
    def __str__(self):
        return self.user.username