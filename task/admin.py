from django.contrib import admin
from . import models


#admin.site.register(models.Task)
@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'priority', 'status', 'created_at', 'slug']
    ordering = ['-created_at']
    list_filter = ['status', 'priority', 'created_at']
    list_editable = ['status', 'priority']
    list_display_links = ['title']
    search_fields = ['title', 'description']
