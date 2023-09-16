from django.db import models
from django.db.models import Count, Avg
from common.models import CommonModel


class TaskGuideline(CommonModel):
    """ TaskGuideline Model definition """

    task_day = models.OneToOneField(
        "task_days.Task_Day",
        on_delete=models.CASCADE,
        related_name="task_guidelines",
    )

    class Meta:
        verbose_name = "Task Guideline"
        verbose_name_plural = "Task Guidelines"

    def __str__(self):
        return f"Guideline for: {self.task_day}"

    @property
    def average_time_taken(self):
        """Calculate the average time taken for completed tasks"""
        evaluations = self.task_day.task_evaluations.filter(is_completed=True)
        avg_time_taken = evaluations.aggregate(
            avg_time=Avg('time_taken'))['avg_time']
        return round(avg_time_taken, 1) if avg_time_taken else None

    @property
    def difficulty_count(self):
        """Count the number of evaluations for each difficulty level"""
        evaluations = self.task_day.task_evaluations.all()
        difficulty_counts = evaluations.values(
            'difficulty').annotate(count=Count('id'))
        return difficulty_counts

    @property
    def top_difficult_questions(self):
        """Find the top 3 most difficult questions"""
        evaluations = self.task_day.task_evaluations.all()
        difficult_question_counts = evaluations.values(
            'difficult_question').annotate(count=Count('id')).order_by('-count')[:3]
        return difficult_question_counts
