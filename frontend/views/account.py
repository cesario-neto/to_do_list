from django.shortcuts import render, redirect
from account.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            redirect('login_view')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'account/pages/register.html', context=context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            form_email = form.data.get('email')
            form_password = form.data.get('password')
            user = authenticate(email=form_email, password=form_password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Email e/ou senha invalido')

    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'account/pages/login.html', context=context)


@login_required(redirect_field_name='next', login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('login_view')
