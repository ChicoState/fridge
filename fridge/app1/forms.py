from django.contrib.auth.forms import UserCreationForm
from app1.models import Item, Profile
from django import forms
from django.contrib.auth.models import User


class ItemForm(forms.ModelForm):
    valid_to = forms.DateField(
        widget = forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'},
            )
    )
    valid_from = forms.DateField(
        widget = forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'},
            )
    )
    class Meta:
        model = Item
        fields = ('food_type', 'food_title', 'photos', 'price', 'quantity', 'valid_from', 'valid_to')

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['valid_from'].help_text = "Example -> mm-dd-yyyy --> 05-07-2016"


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
