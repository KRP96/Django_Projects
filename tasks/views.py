from django import forms
from django.shortcuts import render

tasks = ["foo", "bar", "baz"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")       #this code added the name New Task textbox in add.html while runserver
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=20)   #this code added number increse box in same html

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html", {
        "form":NewTaskForm()
    })