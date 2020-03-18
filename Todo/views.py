from django.shortcuts import render, redirect
from .models import Task
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView, )
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers


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


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskDetailUpdateAPIView(viewsets.GenericViewSet,
                              RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    lookup_field = 'id'


class TaskListCreateAPIView(viewsets.GenericViewSet,
                            ListCreateAPIView):
    serializer_class = TaskListSerializer
    queryset = Task.objects.all()
