from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control rounded-5',
            'placeholder': 'Senha'})
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control rounded-5',
            'placeholder': 'Repita a senha'})

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password1',
            'password2',
        ]
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control rounded-5',
                'placeholder': 'Email',
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control rounded-5',
                'placeholder': 'Nome de Usuário',
            }),
        }


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'required': True,
            'class': 'form-control rounded-5',
            'placeholder': 'Email',
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'required': True,
            'class': 'form-control rounded-5',
            'placeholder': 'Senha',
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
