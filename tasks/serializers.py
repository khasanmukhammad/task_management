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


class TaskAdminSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    task_status = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Task
        fields = ["user", "id", "title", "description", "task_status",
                  "created_at", "updated_at"]


class TaskSearchStatusSerializer(serializers.Serializer):
    task_status = serializers.CharField()
    class Meta:
        model = Task
        fields = ["task_status"]

class TaskCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Task
        fields = ["title", "description", "task_status"]

class TaskStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ["task_status"]



