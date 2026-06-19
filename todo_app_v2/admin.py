from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status']
    search_fields = ['title']
    list_per_page = 10

admin.site.register(Task, TaskAdmin)