from rest_framework import generics, status
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response

from .models import Task
from tasks.serializers import TaskSerializer, TaskCreateSerializer
from shared.custom_pagination import CustomPagination



class TasksListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TasksCreateView(generics.CreateAPIView):
    serializer_class = TaskCreateSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        task = serializer.save(user=request.user)

        return Response(
            {
                "success": True,
                "code": status.HTTP_201_CREATED,
                "task_status": task.task_status,
            },
            status=status.HTTP_201_CREATED
        )