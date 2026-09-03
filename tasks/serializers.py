from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    task_status = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Task
        fields = ["id", "title", "description", "task_status",
            "created_at", "updated_at"]

class TaskCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Task
        fields = ["title", "description", "task_status"]