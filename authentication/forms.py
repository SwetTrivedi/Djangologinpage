from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class signup(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email',]
    


#this is userchange from ya profile ke ander edit optin
from django.contrib.auth.forms import UserChangeForm
class Edituser(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login'] 
        labels={'email':'Email'}
    
# this is userchange form ya admin page 

class EditAdmin(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields='__all__'
        labels={'email':'Email'}