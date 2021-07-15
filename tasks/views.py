from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

#tasks = []            delete this and 

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")       #this code added the name New Task textbox in add.html while runserver
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)   #this code added number increse box in same html

# Create your views here.
def index(request):
    if "tasks" not in  request.session:     #added deleted code in here
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form":NewTaskForm()
    })