from django.forms import ModelForm, CharField, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import CompanySocialMedia

class CompanySocialMediaForm(ModelForm):
   class Meta:
      model = CompanySocialMedia
      fields = '__all__'
   
class CreateUserForm(UserCreationForm):
    username = CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    email = CharField(widget=TextInput(attrs={'placeholder': 'Email'}))
    password1 = CharField(widget=TextInput(attrs={'type': 'password', 'placeholder': ' Password'}))
    password2 = CharField(widget=TextInput(attrs={'type': 'password', 'placeholder': 'Repeat your password'}))
   
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UpdateUserForm(ModelForm):
   class Meta:
      model = User
      fields = ['username', 'email']