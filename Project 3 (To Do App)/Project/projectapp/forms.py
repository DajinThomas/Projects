# movies/forms.py
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task # Name of the database means model name going to edit.
        fields = ['name','task_date'] # fields need to edit in the database
