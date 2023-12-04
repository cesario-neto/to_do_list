from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from task.models import Task
from task.forms import TaskForm
from django.http import Http404
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator


def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'index.html')


@login_required(login_url='/login/')
def home(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    paginator = Paginator(tasks, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'tasks': tasks,
        'page_obj': page_obj,
    }

    return render(request, 'task/pages/home.html', context)


@login_required(login_url='/login/')
def create_task(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            redirect('create_task')

    form = TaskForm()

    context = {
        'form': form
    }

    return render(request, 'task/pages/create_task.html', context)


@login_required(login_url='/login/')
def edit_task(request, task_id):
    try:
        task = Task.objects.select_related('user').get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404()

    if not task.user == request.user:
        raise Http404()

    if request.method == 'POST':
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()

    form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task
    }
    return render(request, 'task/pages/edit_task.html', context)


@login_required(login_url='/login/')
@require_POST
def delete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return Http404()

    if not task.user == request.user:
        raise Http404()

    task.delete()

    return redirect('index')
