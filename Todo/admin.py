from django.contrib import admin
from django.contrib.auth.models import User

from .models import Task


class UserInline(admin.StackedInline):
    model = User
    extra = 0
    max_num = 4


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'complete']
    list_filter = ['complete']
    search_fields = ['title']
    inlines = [UserInline]


admin.site.register(Task, TaskAdmin)
