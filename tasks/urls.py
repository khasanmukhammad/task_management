from django.urls import path
from .views import TasksListView, TasksCreateView, TasksDetailView, ChangeTaskStatusView, \
    TaskSearchStatusView, AdminTasksListView

urlpatterns = [
    path('tasks/', TasksListView.as_view()),
    path('admin/', AdminTasksListView.as_view()),
    path('task-status/', TaskSearchStatusView.as_view()),
    path('create/', TasksCreateView.as_view()),
    path('<uuid:pk>/', TasksDetailView.as_view()),
    path('<uuid:pk>/change-status/', ChangeTaskStatusView.as_view()),

]
