from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class Userdata(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    mobile_number = forms.IntegerField( widget=forms.TextInput())

    class Meta:  
        model=User
        fields=['username','first_name',
        'last_name','email']

class Usedatashow(UserCreationForm):
    password= None
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']

class AdminData(UserCreationForm):
    class Meta:
        model=User
        fields= '__all__'