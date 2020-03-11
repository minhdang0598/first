from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    Data = {'Tasks' : Task.objects.all().order_by("-id")}
    return render(request, 'pages/home.html' , Data)