from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from tasks.serializers import TaskSerializer, TaskCreateSerializer, TaskStatusSerializer,\
    TaskSearchStatusSerializer, TaskAdminSerializer
from shared.custom_pagination import CustomPagination



class TasksListView(generics.ListAPIView):
    serializer_class = TaskAdminSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class AdminTasksListView(generics.ListAPIView):
    serializer_class = TaskAdminSerializer
    permission_classes = (IsAdminUser,)
    custom_pagination_class = CustomPagination

    def get_queryset(self):
        return Task.objects.all()


class TaskSearchStatusView(APIView):
    serializer_class = TaskSearchStatusSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        task_status = request.data.get("task_status")

        task = Task.objects.filter(user=request.user, task_status=task_status)

        serializer = TaskSerializer(task, many=True)
        return Response(
            {
                "success": True,
                "data": serializer.data,
            }
        )


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

class TasksDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def patch(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = self.serializer_class(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "success": True,
                "code": status.HTTP_200_OK,
                "message": "Task updated successfully",
                "data": serializer.data,
            }
        )

    def delete(self, request, *args, **kwargs):
        task = self.get_object()
        task.delete()
        return Response(
            {
                "success": True,
                "message": "Task deleted successfully",
            }
        )


class ChangeTaskStatusView(generics.UpdateAPIView):
    serializer_class = TaskStatusSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def patch(self, request, *args, **kwargs):
        task = self.get_object()

        serializer = self.serializer_class(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "success": True,
                "message": "Task status changed successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK
        )