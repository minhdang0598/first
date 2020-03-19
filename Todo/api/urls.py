from rest_framework import routers
from .views import TaskDetailUpdateAPIView,TaskListCreateAPIView
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'tasks', TaskListCreateAPIView)
router.register(r'tasks', TaskDetailUpdateAPIView)

urlpatterns = [
    path('', include(router.urls)),
]