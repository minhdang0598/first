from Todo.api.serializers import TaskListSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView, )
from rest_framework import viewsets
from ..models import Task


class TaskDetailUpdateAPIView(viewsets.GenericViewSet,
                              RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    lookup_field = 'id'


class TaskListCreateAPIView(viewsets.GenericViewSet,
                            ListCreateAPIView):
    serializer_class = TaskListSerializer
    queryset = Task.objects.all()
