from django import forms
from django.core import validators
from django.contrib.auth.models import User
from myapp.models import foodItem
import datetime
from logging import PlaceHolder

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
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'size': '80'}))
    expiredate = forms.DateField(
        #input_formats = ['%m/%d/%Y'],
        widget = forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'},
            format='%m/%d/%Y')
    )
    
    price = forms.FloatField(widget=forms.TextInput(attrs={'size': '80'}))
    class Meta():
       model = foodItem
       fields = ('description', 'quantity', 'expiredate', 'price')
