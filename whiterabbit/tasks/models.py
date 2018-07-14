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

    def top_unfinished_tasks(self):
        return self.task_set.filter(parent_task__isnull=True, realization__lt=100)

    def unfinished_tasks(self):
        return self.task_set.filter(realization__lt=100).order_by('pk')

    def get_span(self):
        start_dates = [task.start_date for task in self.top_tasks()]
        end_dates = [task.end_date for task in self.top_tasks()]

        if not list(start_dates):
            start_dates = (date.today(),)
        if not list(end_dates):
            end_dates = (date.today(),)

        return min(start_dates), max(end_dates)

    class Meta:
        verbose_name = u'проект'
        verbose_name_plural = u'проекты'


class Task(RandomCard):
    project = models.ForeignKey(Project)
    parent_task = models.ForeignKey('self', blank=True, null=True)
    estimate = models.IntegerField(default=1)
    priority = models.IntegerField(default=0)
    realization = models.IntegerField(default=0)

    @property
    def start_date(self):
        if self.task_set.count() > 0:
            return min(task.start_date for task in self.get_subtasks())
        return date.today() - timedelta(days=7)

    @property
    def end_date(self):
        return self.start_date + timedelta(days=self.get_general_estimate())

    @property
    def to_start(self):
        return self.start_date - date.today()

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
        delta = from_date - self.start_date
        return delta.days + 1

    def get_offset_range(self):
        return range(self.to_start.days)

    def get_days_span(self):
        delta = self.end_date - self.start_date
        return delta.days + 1

    def get_duration_range(self):
        return range(self.get_days_span())

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

    def get_general_estimate(self):
        if self.task_set.count() > 0:
            return sum(task.estimate for task in self.get_subtasks()) + self.estimate
        return self.estimate

    class Meta:
        verbose_name = u'задача'
        verbose_name_plural = u'задачи'
