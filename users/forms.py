from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    '''
    Meta class give nested namespace for configuration and keeps the configuration in one place. And within the configuration we are saying that the model affected will be the User model and on doing "form.save" it will save to user model. The field in the list is the field we want in the form in that order.
    '''
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
