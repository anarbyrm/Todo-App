from django.db.models import fields
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from .forms import TaskFrom
from .models import Task
from django.views.generic import DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy


def home(request):

    tasks = Task.objects.all()
    
    if request.method == 'POST':
        form = TaskFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskFrom()

    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'tasks/list.html', context)


class TaskDetailView(DetailView):
    context_object_name = 'task'
    template_name = 'tasks/detail.html'
    fields = '__all__'

    def get_queryset(self):
        return Task.objects.all()
    

class TaskDeleteView(DeleteView):
    context_object_name = 'task'
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Task.objects.all()



class TaskUpdateView(UpdateView):
    context_object_name = 'task'
    template_name = 'tasks/update.html'
    fields = ['title', 'completed']
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Task.objects.all()