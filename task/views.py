from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import TaskModel
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm()
    return render(request,'task.html',{'form':form})


def edit_task(request,id):
    task = TaskModel.objects.get(pk=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    return render(request,'task.html',{'form':form})

def delete_task(request,id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('homepage')
