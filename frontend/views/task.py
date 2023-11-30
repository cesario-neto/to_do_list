from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from task.models import Task
from account.models import User


def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'index.html')


@login_required(login_url='/login/')
def home(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    print(tasks)

    context = {
        'tasks': tasks
    }

    return render(request, 'task/pages/home.html', context=context)



