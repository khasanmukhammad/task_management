from django.db import models

from shared.models import BaseModel
from users.models import User

NEWLY_ADDED, PENDING, FINISHED =("newly_added", "pending", "finished")

class Task(BaseModel):
    TASK_STATUS = (
        (NEWLY_ADDED, NEWLY_ADDED),
        (PENDING, PENDING),
        (FINISHED, FINISHED),
    )


    title = models.CharField(max_length=100)
    description = models.TextField()
    task_status = models.CharField(max_length=20, choices=TASK_STATUS, default=NEWLY_ADDED)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

