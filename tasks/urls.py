from django.urls import path
from .views import TasksListView, TasksCreateView

urlpatterns = [
    path('tasks/', TasksListView.as_view()),
    path('create/', TasksCreateView.as_view()),
]