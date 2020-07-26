from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist.models import tasklist
from todolist.form import taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def todolist(request):
    if request.method == "POST":
        form = taskform(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manager = request.user
            instance.save()
        messages.success(request,("New Task Added!"))
        return redirect('todolist')
    else:
        all_task = tasklist.objects.filter(manager=request.user)
        paginator = Paginator(all_task, 5)
        page = request.GET.get('pg')
        all_task = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_task': all_task })

def delete_task(request, task_id):
    task = tasklist.objects.get(pk=task_id)
    if task.manager == request.user:
        task.delete()
    else:
        messages.error(request,("You are not allowed to delete this task!"))
    return redirect('todolist')

def edit_task(request, task_id):
    if request.method == "POST":
        task = tasklist.objects.get(pk=task_id)
        form = taskform(request.POST or None, instance = task)
        if form.is_valid():
            form.save()

        messages.success(request,("Task Edited!"))
        return redirect('todolist')
    else:
        task_obj = tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

def complete_task(request, task_id):
    task = tasklist.objects.get(pk=task_id)
    if task.manager == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request,("You are not allowed, dekhte hi goli maar di jayegi!"))
    return redirect('todolist')

def pending_task(request, task_id):
    task = tasklist.objects.get(pk=task_id)
    if task.manager == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request,("You are not allowed, dekhte hi goli maar di jayegi!"))
    return redirect('todolist')

def contact(request):
    context = {
        'contact_text':"welcome to contact page",
        }
    return render(request, 'contact.html', context)

def index(request):
    context = {
        'index_text':"welcome to index page",
        }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'about_text':"welcome to about page",
            }
    return render(request, 'about.html', context)
