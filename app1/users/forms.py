from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()

    # username = forms.CharField(
    #     label='Имя',
    #     widget=forms.TextInput(attrs={
    #         'autofocus': True,
    #         'class': 'form-control',
    #         'placeholder': 'Введите ваше имя'})
    # )
    #
    # password = forms.CharField(
    #     label='Пароль',
    #     widget=forms.TextInput(attrs={
    #         'autocomplete': 'current-password',
    #         'class': 'form-control',
    #         'placeholder': 'Введите ваш пароль'})
    # )


