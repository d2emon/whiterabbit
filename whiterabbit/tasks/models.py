# -*- coding: utf-8 -*-
from randcard.models import RandomCard
from django.db import models
from datetime import date, timedelta


class Project(RandomCard):
    def top_down_tasks(self):
        for task in self.task_set.filter(parent_task__isnull=True).order_by('pk'):
            yield task
            for subtask in task.get_subtasks():
                yield subtask

    def top_tasks(self):
        return self.task_set.filter(parent_task__isnull=True)

    def get_span(self):
        start_date = min(task.start_date for task in self.top_tasks())
        end_date = max(task.end_date for task in self.top_tasks())
        return start_date, end_date

    class Meta:
        verbose_name = u'проект'
        verbose_name_plural = u'проекты'


class Task(RandomCard):
    project = models.ForeignKey(Project)
    parent_task = models.ForeignKey('self', blank=True, null=True)
    priority = models.IntegerField(default=0)
    realization = models.IntegerField(default=0)

    @property
    def start_date(self):
        if self.task_set.count() > 0:
            return min(task.start_date for task in self.get_subtasks())
        return date.today() - timedelta(days=7)

    @property
    def end_date(self):
        if self.task_set.count() > 0:
            return min(task.end_date for task in self.get_subtasks())
        return date.today() + timedelta(days=7)

    def has_subtasks(self):
        return bool(self.task_set.count())

    def get_subtasks(self):
        for subtask in self.task_set.order_by('pk'):
            yield subtask
            for sub in subtask.get_subtasks():
                yield sub

    def get_top_parent_id(self):
        if not self.parent_task:
            return None
        else:
            return self.parent_task.get_top_parent_id() or self.parent_task.id

    def get_offset(self, from_date):
        delta = self.start_date - from_date
        return delta.days + 1

    def get_days_span(self):
        delta = self.start_date - self.end_date
        return delta.days + 1

    def get_realization(self):
        if self.task_set.count() > 0:
            result = []
            for task in self.task_set.all():
                result = result + task.get_realization()
            return result
        else:
            return [min(max(self.realization, 0), 100)]

    def get_general_realization(self):
        all_tasks = self.get_realization()
        value = sum(all_tasks) / len(all_tasks)
        return min(max(value, 0), 100)

    class Meta:
        verbose_name = u'задача'
        verbose_name_plural = u'задачи'
