from django import forms
from django.core import validators
from hospital_app.models import User_profile, UserProfileInfo,User

    

def check_for_value():
    if value[0].lower() != 'z': 
        raise forms.ValidationError("NAME NEEDS TO START WITH Z")
    
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='ENTER YOUR EMAIL AGAIN:')
    text = forms.CharField(widget=forms.Textarea)
    #method of validation and make it hidden from console
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        
        if email != vmail:
            raise forms.ValidationError(" MAKE SURE EMAILS MATCH")

class NewUserForm (forms.ModelForm):
    class Meta():
        model = User_profile
        fields = '__all__'
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User 
        fields = ("username","password","email")
        
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        mdoel = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
        
 