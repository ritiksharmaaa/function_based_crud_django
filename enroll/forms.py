from django import forms 
from . models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['name' , 'email' , 'password']
        widgets = {'name' : forms.TextInput(attrs={'class' : 'form-control'}),
        'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
        'password' : forms.PasswordInput( render_value=True , attrs={'class' : 'form-control'})}
        error_messages = {'name' : {'required' : 'please Provide your name  name '},
        'email' : {'required' : "please Provide your Email"},
         'passowrd' : {'required' : "please Provide your Passowrd "},}