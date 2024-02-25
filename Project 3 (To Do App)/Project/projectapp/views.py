from .forms import TaskForm  # Replace with the actual import path for your form
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task


def task_db(request):
    message = None
    task_detail = Task.objects.all()

    if request.method == "POST":
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        task_date = request.POST.get('task_date', '')

        # Validate form data
        if not name or not priority:
            message = "Please fill in all required fields."
        else:
            # Save data to the database
            new_task = Task(name=name, priority=priority, task_date=task_date)
            new_task.save()
            message = "Data added successfully."

    return render(request, 'index3.html', {'task_detail': task_detail, 'message': message})


# using function view


def task_delete(request, id):
    delete_task = Task.objects.get(id=id)

    if request.method == 'POST':
        delete_task.delete()
        return redirect('/')

    return render(request, 'delete.html', {'task': delete_task})


def task_update(request, id):
    # Retrieve the Task object with the specified ID
    edit_task = Task.objects.get(id=id)

    # Check if the request method is POST
    if request.method == 'POST':
        # Create a TaskForm instance, populating it with data from the Task object
        form = TaskForm(request.POST, instance=edit_task)

        # Check if the form is valid after submitting the data
        if form.is_valid():
            # Save the updated data to the database
            form.save()

            # Add a success message
            messages.success(request, 'Task updated successfully.')

            # Redirect to the desired URL using reverse
            return redirect('/')  # Replace 'task_list' with your actual URL name

    else:
        # If the request method is not POST, create an empty form with Task data
        form = TaskForm(instance=edit_task)

    # Render the template with the form and Task object
    return render(request, 'task_update.html', {'form': form, 'edit_task': edit_task})


from django.views.generic import ListView, CreateView


# Using Class view.


# class index(ListView):
#     model = Task
#     template_name = 'index1.html'
#     context_object_name = 'task_detail'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'index3.html'
    fields = ['name', 'priority', 'task_date']
    success_url = reverse_lazy('task_list')  # replace with the actual success URL name

    def form_valid(self, form):
        # You can add any additional logic here before saving the form
        return super().form_valid(form)


from django.views.generic.detail import DetailView
class TaskDetailView(DetailView):
    model = Task
    template_name = 'class_task_details.html'
    context_object_name = 'task'  # This is already set by default, but it's good to have it explicitly


class TaskListView(ListView): # For listing all tasks
    model = Task
    template_name = 'class_task_list.html'  # Specify the template you want to use
    context_object_name = 'tasks'  # This is the name you'll use in the template to refer to the list of tasks


from django.views.generic import UpdateView


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_update.html'  # Specify the template you want to use
    context_object_name = 'task'
    fields = ['name', 'task_date']

    def get_object(self, queryset=None):
        # Get the Task object based on the pk captured in the URL
        pk = self.kwargs.get('pk', None)
        return get_object_or_404(Task, pk=pk)

    def get_success_url(self):
        # Redirect to the detail view of the updated task after successful update
        return reverse_lazy('index_detail', kwargs={'pk': self.object.pk})


from django.views.generic import DeleteView


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'  # Specify the template you want to use
    context_object_name = 'task'

    def get_object(self, queryset=None):
        # Get the Task object based on the pk captured in the URL
        pk = self.kwargs.get('pk', None)
        return get_object_or_404(Task, pk=pk)

    def get_success_url(self):
        # Redirect to a specific URL after successful deletion
        return reverse_lazy('task_list')  # Adjust 'task-list' to your task list view name

