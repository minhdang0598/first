from django.shortcuts import render, redirect
from .models import Task
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
import requests

"""
def index(request):
    data = {'Tasks': Task.objects.all().order_by("-id")}
    if request.method == "POST":
        if "add" in request.POST:
            title = request.POST["taskTitle"]
            task = Task(title=title, complete=False)
            task.save()
            return redirect("/")
        if "done" in request.POST:
            task = Task.objects.get(id=request.POST["done"])
            task.complete = True
            task.save()
        if "undone" in request.POST:
            task = Task.objects.get(id=request.POST["undone"])
            task.complete = False
            task.save()
        if "delete" in request.POST:
            task = Task.objects.get(id=request.POST["delete"])
            task.delete()

    return render(request, 'pages/home.html', data)
"""


def index(request):
    url = 'http://localhost:8000/api/tasks'
    data= requests.get(url+'?user='+str(request.user.id)).json()
    if request.method == "POST":
        if "add" in request.POST:
            title = request.POST["taskTitle"]
            task = {'title': title, 'complete': False, 'user': request.user.id}
            requests.post(url, task)
            data= requests.get(url+'?user='+str(request.user.id)).json()
            redirect('/')
        if "done" in request.POST:
            idd = request.POST["done"]
            title = Task.objects.get(id=idd).title
            task = {'id': idd, 'title': title, 'complete': True, 'user': request.user.id}
            requests.put(url + idd + '/', task)
            data = requests.get(url + '?user=' + str(request.user.id)).json()
            redirect('/')
        if "undone" in request.POST:
            idd = request.POST["undone"]
            title = Task.objects.get(id=idd).title
            task = {'id': idd, 'title': title, 'complete': False, 'user': request.user.id}
            requests.put(url + idd + '/', task)
            data = [obj for obj in requests.get(url).json() if(obj['user'] == request.user.id)]
            redirect('/')
        if "delete" in request.POST:
            idd = request.POST["delete"]
            requests.delete(url + idd + '/')
            data= requests.get(url+'?user='+str(request.user.id)).json()
            redirect('/')

    return render(request, 'pages/home.html', {'Tasks': data, })


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})
