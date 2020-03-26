from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'complete', 'user']
    list_filter = ['complete']
    search_fields = ['title']


class TaskInline(admin.StackedInline):
    model = Task
    can_delete = False
    extra = 1
    max_num = 4
    verbose_name_plural = 'Task Inline'


class UserAdmin(BaseUserAdmin):
    inlines = (TaskInline,)


admin.site.register(Task, TaskAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)