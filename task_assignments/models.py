from django.db import models
from common.models import CommonModel


class TaskAssignment(CommonModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="task_assignments")
    task_day = models.ForeignKey(
        "task_days.Task_Day", on_delete=models.CASCADE, related_name="task_assignments")
    assigned_date = models.DateField()

    def __str__(self):
        return f"Assignment of {self.task_day} to {self.user} on {self.assigned_date}"