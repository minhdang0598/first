from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def index(request):
    Tasks = {'Tasks' : Task.objects.all().order_by("-id")}
    if request.method == "POST":
        if "add" in request.POST:
            title = request.POST["taskTitle"]
            task = Task(title = title,complete = False)
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
            checkedlist = request.POST["checkedbox"]
            for task_id in checkedlist:
                task = Task.objects.get(id=int(task_id))
                task.delete()
    return render(request, 'pages/home.html' , Tasks)