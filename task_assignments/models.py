from django.db import models
from common.models import CommonModel


class TaskAssignment(CommonModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="task_assignments")
    task_day = models.ForeignKey(
        "task_days.Task_Day", on_delete=models.CASCADE, related_name="task_assignments")
    assigned_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    n_day = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Assignment of {self.task_day} to {self.user} on {self.assigned_date}"
