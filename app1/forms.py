from django import forms
from .models import TaskModel


# creating a form
class TaskForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = TaskModel

        # specify fields to be used
        fields = [

            "task",
            "description",
        ]
