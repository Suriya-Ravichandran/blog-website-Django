from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class ContactForm(forms.Form):
    name=forms.CharField(label="Name",max_length=100,required=True)
    email=forms.EmailField(label="Email",required=True)
    message=forms.CharField(label="Message",required=True)

class SignupForm(forms.ModelForm):
    username=forms.CharField(label="Username",max_length=100,required=True)
    email=forms.CharField(label="Email",max_length=100,required=True)
    password=forms.CharField(label="Password",max_length=100,required=True)
    confirmpassword=forms.CharField(label="ConfirmPassword",max_length=100,required=True)

    class Meta:
        model= User
        fields= ['username',"email","password"]
    
    def clean(self):
        cleaned_data=super().clean()
        password =cleaned_data.get("password")
        password_confirm=cleaned_data.get("confirmpassword")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Password Not Match")
        
