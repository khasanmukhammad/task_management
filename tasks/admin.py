from django.contrib import admin

from tasks.models import Task


@admin.register(Task)


class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "user",
        "task_status",
        "created_at",
        "updated_at",
    ]

    list_filter = ["task_status"]

    search_fields = ["title", "description"]

    ordering = ["-created_at"]
