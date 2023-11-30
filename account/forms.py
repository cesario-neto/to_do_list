from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'required': True,
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'required': True
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not User.objects.filter(email__exact=email).exists():
            # self.add_error('email', 'Email ou senha invalida')
            raise ValidationError(
                'Email e/ou senha invalida',
                code='invalid'
            )

        return email
