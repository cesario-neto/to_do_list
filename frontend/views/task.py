from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'index.html')


@login_required(login_url='/login/')
def home(request):

    return render(request, 'task/pages/home.html')
