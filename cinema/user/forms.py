from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser


class RegistrationForm(UserCreationForm):
    age = forms.IntegerField()
    name = forms.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'age', 'name')