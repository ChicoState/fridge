from django import forms
from django.core import validators
from django.contrib.auth.models import User
from myapp.models import foodItem


class JoinForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'size': '30'}))
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        help_texts = {
            'username': None
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class FoodItemForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    expiredate = forms.IntegerField(widget=forms.TextInput(attrs={'size': '80'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'size': '80'}))
    class Meta():
       model = foodItem
       fields = ('description', 'expiredate', 'price')
