from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, HttpResponseRedirect
import random

# Create your views here.
from django.views.decorators.csrf import csrf_protect

from .models import TaskModel
from .forms import TaskForm

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    # add the dictionary during initialization
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    dataset=TaskModel.objects.all()
    context={'form':form,'dataset': dataset }
    return render(request, "create_view.html", context)

def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = TaskModel.objects.get(id=id)

    return render(request, "detail_view.html", context)


# update view for details
def update_view(request, id):
    context = {}
    obj = get_object_or_404(TaskModel, id=id)

    form = TaskForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

        # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(TaskModel, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)


