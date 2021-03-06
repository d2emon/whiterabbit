# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from tasks.models import Project
from datetime import timedelta
from copy import copy

username = "МихалычЪ"


def _day_generator(start):
    start_date = copy(start)
    while True:
        yield start_date
        start_date = start_date + timedelta(days=1)


def index(request):
    return render(request, 'tasks/index.html', {
        "username": username,
        'projects': Project.objects.all(),
    })


def project(request, project):
    project = get_object_or_404(Project, pk=project)

    # Test wrong team
    # Test wrong user

    project_start, project_end = project.get_span()
    delta = project_end - project_start
    gen = _day_generator(project_start)
    project_span = []
    for i in range(delta.days + 1):
        project_span.append(gen.next)

    graph = []
    for task in project.top_down_tasks():
        graph.append({
            'task': task,
            'offset': range(task.get_offset(project_start)),
            'duration': range(task.get_days_span()),
            'has_subtasks': task.has_subtasks(),
            'realization': task.get_general_realization(),
        })

    top_tasks = []
    sub_tasks = {}
    for task in project.top_down_tasks():
        top_id = task.get_top_parent_id()
        if top_id is None:
            top_tasks.append(task)
        else:
            if top_id not in sub_tasks:
                sub_tasks[top_id] = []
            sub_tasks[top_id].append(task)

    top_sub_tasks = []
    for task in project.top_tasks():
        top_sub_tasks.append({
            'task': task,
            'subtasks': sub_tasks.get(task.id),
        })
    return render(request, 'tasks/project.html', {
        'project': project,
        'project_span': project_span,
        'day_span': range(7),
        'graph': graph,
        'tasks': top_sub_tasks,
    })
