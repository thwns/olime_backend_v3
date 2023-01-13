from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def see_all_tasks(request):
    return HttpResponse("hello!")


def see_one_task(request, task_id):
    return HttpResponse(f"see task with id: {task_id}")
